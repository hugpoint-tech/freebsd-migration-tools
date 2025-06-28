package forgejo

import (
	"testing"

	"code.gitea.io/sdk/gitea"
)

func TestGetUser(t *testing.T) {
	giteaClient := New(DEFAULT_GITEA_URL)

	user, _, err := giteaClient.client.GetMyUserInfo()
	if err != nil {
		t.Fatalf("Failed to fetch user information: %v", err)
	}

	if user.UserName == "" {
		t.Fatal("User login is empty")
	}

	if user.Email == "" {
		t.Fatal("User email is empty")
	}

	t.Logf("User ID: %d\n", user.ID)
	t.Logf("Login: %s\n", user.UserName)
	t.Logf("Full Name: %s\n", user.FullName)
	t.Logf("Email: %s\n", user.Email)
}

func TestListMyRepos(t *testing.T) {
	giteaClient := New(DEFAULT_GITEA_URL)

	repos, _, err := giteaClient.client.ListMyRepos(gitea.ListReposOptions{
		ListOptions: gitea.ListOptions{
			Page:     1,
			PageSize: 10},
	})

	if err != nil {
		t.Fatalf("Failed to fetch repositories: %v", err)
	}

	if len(repos) == 0 {
		t.Log("No repositories found.")
	} else {
		for _, repo := range repos {
			t.Logf("Repository ID: %d, FullName: %s\n", repo.ID, repo.FullName)
		}
	}
}

func TestListMyOrgs(t *testing.T) {
	giteaClient := New(DEFAULT_GITEA_URL)

	orgs, _, err := giteaClient.client.ListMyOrgs(gitea.ListOrgsOptions{
		ListOptions: gitea.ListOptions{
			Page:     1,
			PageSize: 10},
	})

	if err != nil {
		t.Fatalf("Failed to fetch organizations: %v", err)
	}

	if len(orgs) == 0 {
		t.Log("No organizations found.")
	} else {
		for _, org := range orgs {
			t.Logf("Organization ID: %d, Login: %s\n", org.ID, org.UserName)
		}
	}
}

func TestListMyTeams(t *testing.T) {
	giteaClient := New(DEFAULT_GITEA_URL)

	teams, _, err := giteaClient.client.ListMyTeams(&gitea.ListTeamsOptions{
		ListOptions: gitea.ListOptions{
			Page:     1,
			PageSize: 10,
		},
	})
	if err != nil {
		t.Fatalf("Failed to fetch teams: %v", err)
	}

	if len(teams) == 0 {
		t.Log("No teams found.")
	} else {
		for _, team := range teams {
			t.Logf("Team ID: %d, Name: %s, Description: %s, Organization: %s\n", team.ID, team.Name, team.Description, team.Organization.UserName)
		}
	}
}

func TestListMyFollowers(t *testing.T) {
	giteaClient := New(DEFAULT_GITEA_URL)

	followers, _, err := giteaClient.client.ListMyFollowers(gitea.ListFollowersOptions{
		ListOptions: gitea.ListOptions{
			Page:     1,
			PageSize: 10},
	})

	if err != nil {
		t.Fatalf("Failed to fetch followers: %v", err)
	}

	if len(followers) == 0 {
		t.Log("No followers found.")
	} else {
		for _, fol := range followers {
			t.Logf("Follower ID: %d, Name: %s, Full Name: %s, Email: %s\n", fol.ID, fol.UserName, fol.FullName, fol.Email)
		}
	}
}
