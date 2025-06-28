package forgejo

import (
	"code.gitea.io/sdk/gitea"
	"fmt"
	"hugpoint.tech/freebsd/migrator/bugzilla"
	"hugpoint.tech/freebsd/migrator/util"
	"os"
)

const (
	ENV_GITEA_TOKEN = "GITEA_TOKEN"
	ENV_REPO_NAME   = "REPO_NAME"
	ENV_REPO_OWNER  = "REPO_OWNER"

	DEFAULT_GITEA_URL = "https://gitcvt.hugpoint.tech"
)

type Gitea struct {
	client *gitea.Client

	RepoName  string
	RepoOwner string
}

func New(url string) Gitea {
	apiToken := os.Getenv(ENV_GITEA_TOKEN)
	if apiToken == "" {
		util.Fatalf("%s environment variable is not set", ENV_GITEA_TOKEN)
	}

	client, err := gitea.NewClient(url, gitea.SetToken(apiToken))
	util.CheckFatal("error creating Gitea client", err)

	repoOwner := os.Getenv(ENV_REPO_OWNER)
	repoName := os.Getenv(ENV_REPO_NAME)

	if repoOwner == "" || repoName == "" {
		util.Fatalf("%s and %s environment variables must be set", ENV_REPO_OWNER, ENV_REPO_NAME)
	}

	return Gitea{
		client:    client,
		RepoName:  repoName,
		RepoOwner: repoOwner,
	}
}

// TODO move database logic into database package
//func (g *Gitea) UploadBugs(bc *sqlite.Conn) {
//
//	stmt, err := prepareStmt(bc)
//	util.CheckFatal("failed to prepare statement", err)
//	defer stmt.Finalize()
//
//	err = g.processBugRows(stmt)
//	util.CheckFatal("error processing bug rows", err)
//}
//
//func prepareStmt(db *sqlite.Conn) (*sqlite.Stmt, error) {
//	stmt, err := db.Prepare("SELECT OtherFieldsJSON FROM bugs")
//	if err != nil {
//		return nil, fmt.Errorf("failed to prepare statement: %w", err)
//	}
//	return stmt, nil
//}

func (g *Gitea) createGiteaIssue(bug bugzilla.Bug, rawJSON string) error {
	issueBody := fmt.Sprintf(
		"ID: %d\n\nCreation Time: %s\n\nCreator: %s\n\nDetails:\n%s\n",
		bug.ID, bug.CreationTime, bug.Creator, rawJSON,
	)

	issue, _, err := g.client.CreateIssue(g.RepoOwner, g.RepoName, gitea.CreateIssueOption{
		Title: bug.Summary,
		Body:  issueBody,
	})
	if err != nil {
		return fmt.Errorf("failed to create issue: %w", err)
	}
	fmt.Printf("Issue created: %s\n", issue.URL)
	return nil
}

//func (g *Gitea) processBugRows(stmt *sqlite.Stmt) error {
//	for {
//		hasRow, err := stmt.Step()
//		if err != nil {
//			return fmt.Errorf("failed to step through rows: %w", err)
//		}
//		if !hasRow {
//			break
//		}
//
//		OtherFieldsJSON := stmt.ColumnText(0)
//
//		var bug Bug
//		if err := json.Unmarshal([]byte(OtherFieldsJSON), &bug); err != nil {
//			fmt.Printf("Failed to parse JSON for row %d: %v\nData: %s", stmt.ColumnInt(0), err, OtherFieldsJSON)
//			continue
//		}
//
//		if err := g.createGiteaIssue(bug, OtherFieldsJSON); err != nil {
//			fmt.Printf("Failed to process bug ID %d: %v\nData: %s", bug.ID, err, OtherFieldsJSON)
//			continue
//		}
//	}
//	return nil
//}
