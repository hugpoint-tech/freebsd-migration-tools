package bugzilla

import (
	"encoding/json"
	"fmt"
	"sort"
	"strconv"
	"strings"

	"hugpoint.tech/freebsd/migrator/util"
	"io"
	"log"
	"net/http"
	"net/url"
	"os"
)

type Client struct {
	token string
	URL   string
	http  *http.Client
}

type loginResponse struct {
	Id    int    `json:"id"`
	Token string `json:"token"`
}

func New() Client {
	login := os.Getenv("BUGZILLA_LOGIN")
	password := os.Getenv("BUGZILLA_PASSWORD")
	if login == "" || password == "" {
		log.Fatal("BUGZILLA_LOGIN or BUGZILLA_PASSWORD is not set")
	}

	bc := Client{
		URL:   "https://bugs.freebsd.org/bugzilla/rest",
		token: "",
		http:  &http.Client{},
	}

	formData := url.Values{}
	formData.Set("login", login)
	formData.Set("password", password)

	response, err := bc.http.Get(bc.URL + "/login?" + formData.Encode())
	util.CheckFatal("login and/or password incorrect", err)

	defer response.Body.Close()

	if response.StatusCode != http.StatusOK {
		util.Fatalf("login failed, status code: %d", response.StatusCode)
	}

	var loginResponse loginResponse
	err = json.NewDecoder(response.Body).Decode(&loginResponse)
	util.CheckFatal("error reading bugzilla login response body", err)

	if loginResponse.Token == "" {
		util.Fatal("login token is empty")
	}
	bc.token = loginResponse.Token

	return bc
}

func (client *Client) GetBugs(bugIds []int) ([]Bug, error) {

	if bugIds == nil || len(bugIds) == 0 {
		return nil, fmt.Errorf("bugIds is nil or empty")
	}

	sort.Slice(bugIds, func(i, j int) bool {
		return bugIds[i] < bugIds[j]
	})

	bugIdStr := make([]string, 0, len(bugIds))
	for _, id := range bugIds {
		bugIdStr = append(bugIdStr, strconv.Itoa(id))
	}

	baseURL, err := url.Parse(fmt.Sprintf("%s/bug", client.URL))
	if err != nil {
		return nil, fmt.Errorf("failed to parse base URL: %w", err)
	}

	params := url.Values{}
	params.Set("id", strings.Join(bugIdStr, ","))
	baseURL.RawQuery = params.Encode()

	req, err := http.NewRequest("GET", baseURL.String(), nil)
	if err != nil {
		return nil, fmt.Errorf("failed to create request: %w", err)
	}

	req.Header.Set("Authorization", fmt.Sprintf("Token %s", client.token))
	resp, err := client.http.Do(req)
	if err != nil {
		return nil, fmt.Errorf("failed to execute request: %w", err)
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return nil, fmt.Errorf("unexpected status code: %d", resp.StatusCode)
	}

	var result struct {
		Bugs []Bug `json:"bugs"`
	}

	if err := json.NewDecoder(resp.Body).Decode(&result); err != nil {
		return nil, fmt.Errorf("failed to decode response: %w", err)
	}

	sort.Slice(result.Bugs, func(i, j int) bool {
		return result.Bugs[i].ID < result.Bugs[j].ID
	})

	return result.Bugs, nil
}

func (client *Client) GetComments(bugID int) ([]Comment, error) {

	apiURL := fmt.Sprintf("%s/bug/%d/comment", client.URL, bugID)
	params := url.Values{}
	params.Set("token", client.token)
	fullURL := apiURL + "?" + params.Encode()
	response, err := client.http.Get(fullURL)

	if err != nil {
		return nil, fmt.Errorf("error making GET request to %s: %v", fullURL, err)
	}
	defer response.Body.Close()

	switch {
	case response.StatusCode >= 100 && response.StatusCode <= 399:
	// nop, all good
	//case response.StatusCode == 429:
	// TOO Many Requests.
	//case response.StatusCode == 503:
	//	// TODO retry
	default:
		return nil, fmt.Errorf("comment request error: %s", response.Status)
	}

	body, err := io.ReadAll(response.Body)
	if err != nil {
		return nil, fmt.Errorf("error reading response body from %s: %v", fullURL, err)
	}

	var commentsResponse CommentsResponse

	if err := json.Unmarshal(body, &commentsResponse); err != nil {
		return nil, fmt.Errorf("error decoding JSON: %v", err)
	}

	return commentsResponse.Bugs[int(bugID)].Comments, nil
}

func (client *Client) GetAttachments(bugID int) ([]Attachment, error) {
	apiURL := fmt.Sprintf("%s/bug/%d/attachment", client.URL, bugID)
	params := url.Values{}
	params.Set("token", client.token)

	fullURL := apiURL + "?" + params.Encode()
	response, err := client.http.Get(fullURL)
	if err != nil {
		return nil, fmt.Errorf("error making GET request to %s: %v", fullURL, err)
	}
	defer response.Body.Close()

	body, err := io.ReadAll(response.Body)
	if err != nil {
		return nil, fmt.Errorf("error reading response body from %s: %v", fullURL, err)
	}

	var attachmentsResponse AttachmentsResponse
	if err := json.Unmarshal(body, &attachmentsResponse); err != nil {
		return nil, fmt.Errorf("error decoding JSON: %v", err)
	}

	return attachmentsResponse.Bugs[int(bugID)], nil
}
