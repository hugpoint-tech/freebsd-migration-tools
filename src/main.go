package main

import (
	"fmt"
	"hugpoint.tech/freebsd/migrator/bugzilla"
	"hugpoint.tech/freebsd/migrator/forgejo"
	"hugpoint.tech/freebsd/migrator/util"
	"os"
	"path/filepath"
	"time"
)

func main() {

	if len(os.Args) < 2 {
		fmt.Println("not enough arguments. use help")
		return
	}
	command := os.Args[1]

	bugzClient := bugzilla.New()

	datadir, err := filepath.Abs("./data")
	if err != nil {
		panic(err)
	}

	switch command {
	case "bugzilla-download-bugs":
		startTime := time.Now()
		bugzilla.DownloadBugs(&bugzClient, datadir)
		duration := time.Since(startTime)
		fmt.Printf("bugs downloaded in %s\n", duration)
	case "help":
		printHelp()

	case "bugzilla-download-users":
		// TODO extract users from bugs and comments
		break

	case "bugzilla-download-comments":
		startTime := time.Now()
		err = bugzilla.DownloadComments(&bugzClient, datadir)
		util.CheckFatal("failed to download comments", err)
		duration := time.Since(startTime)
		fmt.Printf("comments downloaded in %s\n", duration)

	case "bugzilla-download-attachments":
		startTime := time.Now()
		err = bugzilla.DownloadAttachments(&bugzClient, datadir)
		util.CheckFatal("failed to download attachments", err)
		duration := time.Since(startTime)
		fmt.Printf("attachments downloaded in in %s\n", duration)

	case "gitea-upload-bugs":

		var url string
		if len(os.Args) < 3 {
			url = forgejo.DEFAULT_GITEA_URL
			fmt.Println("using default gitea url", url)
		} else {
			url = os.Args[2]
		}
		// TODO fix this after gitea is decoupled from database
		//giteaClient := giteacustom.New(url)
		//giteaClient.UploadBugs(db.Conn)

	default:
		fmt.Println("invalid command")
		printHelp()
	}
}

func printHelp() {
	fmt.Println("available commands:\n" +
		"bugzilla-download-bugs - Downloads bugs from bugzilla\n" +
		"bugzilla-show-bugs - Shows bugzilla bugs\n" +
		"bugzilla-download-users - Downloads users from bugzilla\n" +
		"bugzilla-download-comments - Downloads comments from bugs db. Can take long time ~16+ hours.\n" +
		"bugzilla-download-attachments - Downloads attachments from bugs db. Can take long time ~16+ hours.\n" +
		"gitea-upload-bugs [url] - Uploads bugs to gitea from local bugzilla db\n" +
		"help - shows available commands")
}
