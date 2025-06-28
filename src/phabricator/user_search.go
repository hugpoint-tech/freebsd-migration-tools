package phabricator

import (
	"encoding/json"
	"fmt"
	"net/http"
	"net/url"

	. "hugpoint.tech/freebsd/migrator/util"
)

type UserSearchAPI struct {
	client *PhabClient
	method string
	params url.Values
}

func (p *PhabClient) UserSearch() *UserSearchAPI {
	result := &UserSearchAPI{
		method: "user.search",
		client: p,
		params: make(url.Values),
	}

	result.params.Set("api.token", p.token)
	return result
}

func (p *UserSearchAPI) Get() []User {
	p.params.Set("order", "oldest")
	p.params.Set("limit", "100")

	result := []User{}
	for {
		userResponse := UserResponse{}
		resp, err := http.PostForm(p.client.url+p.method, p.params)
		CheckFatal("UserSearchAPI get", err)

		err = json.NewDecoder(resp.Body).Decode(&userResponse)
		CheckFatal("UserSearchAPI get", err)

		if userResponse.ErrorCode != "" {
			panic(userResponse.ErrorInfo)
		}

		result = append(result, userResponse.Result.Users...)
		resp.Body.Close()

		fmt.Printf("\rReading phab users: %d", len(result))

		if userResponse.Result.Cursor.After != "" {
			p.params.Set("after", userResponse.Result.Cursor.After)
		} else {
			p.params.Del("after")
			break
		}
	}
	fmt.Println()

	return result
}
