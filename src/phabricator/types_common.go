package phabricator

type Cursor struct {
	After  string `json:"after"`
	Before string `json:"before"`
	Limit  string `json:"limit"`
	Order  string `json:"order"`
}
