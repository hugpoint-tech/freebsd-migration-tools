package bugzilla

import (
	"bufio"
	_ "context"
	"encoding/json"
	"fmt"
	"maps"
	"os"
	"path/filepath"
	"sort"
	"strconv"
	"strings"
	"sync"
)

const (
	workerCount   = 10
	pageSizeLimit = 100
	expectedBugs  = 288000
)

type worker struct {
	id      int
	client  *Client
	wg      *sync.WaitGroup
	errors  map[int]bool
	dataDir string
}

func (w *worker) downloadBugs(limit int) {
	defer w.wg.Done()
	i := 0

	// worker ids start with 0 but bugs start with 1
	start := w.id*limit + 1
	for {

		shift := i * limit * workerCount
		offset := start + shift

		if offset > expectedBugs {
			break
		}

		bugIds := make([]int, 0, expectedBugs)
		for i := offset; i < offset+limit; i++ {
			if i > expectedBugs {
				continue
			}
			bugIds = append(bugIds, i)
		}

		bugs, err := w.client.GetBugs(bugIds)
		if err != nil {
			fmt.Printf("worker %d failed to download bugs [%s] %s\n", w.id, err)
			for _, bug := range bugs {
				w.errors[bug.ID] = true
			}

			continue
		}

		for _, bug := range bugs {

			var bytes []byte
			bytes, err = json.MarshalIndent(bug, "", "  ")
			dir := filepath.Join(w.dataDir, strconv.Itoa(bug.ID/1000), strconv.Itoa(bug.ID))
			err = os.MkdirAll(dir, 0o755)
			if err != nil {
				fmt.Printf("worker %d failed to make directory for bug %d: %s\n", w.id, bug.ID, err)
				w.errors[bug.ID] = true
				continue
			}
			filename := filepath.Join(dir, fmt.Sprintf("bug-%d.json", bug.ID))

			err = os.WriteFile(filename, bytes, 0o644)
			if err != nil {
				fmt.Printf("worker %d failed to save bug %d: %s\n", w.id, bug.ID, err)
				w.errors[bug.ID] = true
				continue
			}
		}

		fmt.Printf("worker %d iteration %d downloaded %d bugs %d-%d\n", w.id, i, len(bugs), offset, offset+limit-1)

		missing := findMissingBugIDs(bugIds, bugs)
		for _, id := range missing {
			fmt.Println("Missing bug", id)
		}

		if offset+limit > expectedBugs {
			break
		}

		i++
	}

	fmt.Printf("Worker %d: finished\n", w.id)
	return
}

func (w *worker) downloadComment(in <-chan int) {
	defer w.wg.Done()

	for bugid := range in {
		comments, err := w.client.GetComments(bugid)
		if err != nil {
			fmt.Printf("Worker %d: failed to download comments for bug %d: %s\n", w.id, bugid, err)
			w.errors[bugid] = true
			continue
		}

		for _, comment := range comments {
			var bytes []byte
			bytes, err = json.MarshalIndent(comment, "", " ")
			dir := filepath.Join(w.dataDir, strconv.Itoa(comment.BugID/1000), strconv.Itoa(comment.BugID))
			filename := filepath.Join(dir, fmt.Sprintf("comment-%d-%d.json", comment.BugID, comment.ID))

			err = os.WriteFile(filename, bytes, 0o644)
			if err != nil {
				w.errors[comment.BugID] = true
				continue
			}
		}
		fmt.Printf("worker %d downloaded %d comments for bug %d\n", w.id, len(comments), bugid)
	}
	fmt.Printf("worker %d finished\n", w.id)
}

func (w *worker) downloadAttachment(in <-chan int) {
	defer w.wg.Done()

	for bugid := range in {
		attachments, err := w.client.GetAttachments(bugid)
		if err != nil {
			fmt.Printf("worker %d failed to download attachments for bug %d: %s\n", w.id, bugid, err)
			w.errors[bugid] = true
			continue
		}

		for _, a := range attachments {
			var bytes []byte
			bytes, err = json.MarshalIndent(a, "", " ")
			if err != nil {
				fmt.Printf("worker %d: failed to download attachment %d for bug %d: %s\n", w.id, a.ID, a.BugID, err)
				w.errors[a.BugID] = true
				continue
			}

			dir := filepath.Join(w.dataDir, strconv.Itoa(a.BugID/1000), strconv.Itoa(a.BugID))
			filename := filepath.Join(dir, fmt.Sprintf("attachment-%d-%d.json", a.BugID, a.ID))
			err = os.WriteFile(filename, bytes, 0o644)
			if err != nil {
				fmt.Printf("worker %d: failed to save attachment %d for bug %d: %s\n", w.id, a.ID, a.BugID, err)
				w.errors[a.BugID] = true
				continue
			}
		}
		fmt.Printf("worker %d downloaded %d attachments for bug %d\n", w.id, len(attachments), bugid)
	}

	fmt.Printf("%d finished\n", w.id)
}

func DownloadBugs(client *Client, dataDir string) error {
	var wg sync.WaitGroup
	var totalErrors int

	dir := filepath.Join(dataDir, "bugzilla")
	err := os.MkdirAll(dir, 0o755)
	if err != nil {
		return err
	}

	workers := make([]worker, workerCount)
	for idx := 0; idx < workerCount; idx++ {
		w := worker{
			id:      idx,
			client:  client,
			wg:      &wg,
			dataDir: dir,
		}
		workers[idx] = w
		wg.Add(1)

		go w.downloadBugs(pageSizeLimit)
	}
	wg.Wait()

	for _, w := range workers {
		fmt.Printf("worker %d: finished with total errors: %d\n", w.id, len(w.errors))
		totalErrors += len(w.errors)
	}

	fmt.Printf("Total bug download errors: %d\n", totalErrors)
	return nil
}

func DownloadComments(bugz *Client, dataDir string) error {

	var wg sync.WaitGroup
	var totalErrors int

	idChan := make(chan int)
	workers := make([]worker, 0, workerCount)

	dir := filepath.Join(dataDir, "bugzilla")
	bugIds, err := getDownloadedBugs(dir)
	if err != nil {
		return err
	}

	for idx := range cap(workers) {
		w := worker{
			id:      idx,
			client:  bugz,
			wg:      &wg,
			dataDir: dir,
		}
		workers = append(workers, w)
		wg.Add(1)
	}

	for _, d := range workers {
		go d.downloadComment(idChan)
	}

	for _, id := range bugIds {
		idChan <- id
	}
	close(idChan)
	wg.Wait()

	allErrors := make(map[int]bool)
	for _, w := range workers {
		fmt.Printf("Worker %d: finished with %d total errors\n", w.id, len(w.errors))
		maps.Copy(w.errors, allErrors)
		totalErrors += len(w.errors)
	}

	err = writeMapKeysToFile("comments-errors.txt", allErrors)
	if err != nil {
		return err
	}
	fmt.Printf("Total comments download errors: %d\n", totalErrors)
	return nil
}

func DownloadAttachments(client *Client, dataDir string) error {

	var wg sync.WaitGroup
	var totalErrors int

	dir := filepath.Join(dataDir, "bugzilla")

	bugIds, err := getDownloadedBugs(dir)
	if err != nil {
		return err
	}

	idChan := make(chan int, workerCount)
	workers := make([]worker, 0, workerCount)

	for idx := range cap(workers) {
		w := worker{
			id:      idx,
			client:  client,
			wg:      &wg,
			dataDir: dir,
		}
		workers = append(workers, w)
		wg.Add(1)
	}

	for _, d := range workers {
		go d.downloadAttachment(idChan)
	}

	for _, id := range bugIds {
		idChan <- id
	}
	close(idChan)
	wg.Wait()

	for _, w := range workers {
		fmt.Printf("worker %w finished with %w errors\n", w.id, len(w.errors))
		totalErrors += len(w.errors)
	}

	fmt.Printf("Total attachments download errors %w\n", totalErrors)
	return nil
}

func findMissingBugIDs(requiredIds []int, received []Bug) []int {
	receivedMap := make(map[int]bool)
	for _, bug := range received {
		receivedMap[bug.ID] = true
	}

	var missing []int
	for _, id := range requiredIds {
		if !receivedMap[id] {
			missing = append(missing, id)
		}
	}

	return missing
}

func getDownloadedBugs(rootDir string) ([]int, error) {
	bugIds := make([]int, 0, expectedBugs)

	err := filepath.WalkDir(rootDir, func(path string, d os.DirEntry, err error) error {

		if err != nil {
			fmt.Printf("Error accessing %s: %v\n", path, err)
			return err
		}

		if d.IsDir() {
			return nil
		}

		filename := filepath.Base(path)

		if !strings.HasPrefix(filename, "bug-") {
			return nil
		}

		if !strings.HasSuffix(filename, ".json") {
			return nil
		}

		num := filename
		num = strings.TrimSuffix(num, ".json")
		num = strings.TrimPrefix(num, "bug-")

		var id int
		id, err = strconv.Atoi(num)
		if err != nil {
			return err
		}

		bugIds = append(bugIds, id)

		return nil
	})

	sort.Ints(bugIds)

	return bugIds, err
}

func writeMapKeysToFile(filename string, errors map[int]bool) error {
	file, err := os.Create(filename)
	if err != nil {
		return fmt.Errorf("failed to create file: %w", err)
	}
	defer file.Close()
	writer := bufio.NewWriter(file)
	defer writer.Flush()

	for key := range errors {
		_, err := writer.WriteString(strconv.Itoa(key) + "\n")
		if err != nil {
			return fmt.Errorf("failed to write key: %w", err)
		}
	}

	return nil
}
