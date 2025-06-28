package phabricator

type UserPolicy struct {
	Edit string `json:"edit"`
	View string `json:"view"`
}

type User struct {
	ID     int        `json:"id"`
	Type   string     `json:"type"`
	Phid   string     `json:"phid"`
	Fields UserFields `json:"fields"`
}

type UserFields struct {
	Username     string     `json:"username"`
	RealName     string     `json:"realName"`
	DateCreated  int        `json:"dateCreated"`
	DateModified int        `json:"dateModified"`
	Roles        []string   `json:"roles"`
	Policy       UserPolicy `json:"policy"`
}

type UserResult struct {
	Cursor Cursor `json:"cursor"`
	Users  []User `json:"data"`
}

type UserResponse struct {
	ErrorCode string     `json:"error_code"`
	ErrorInfo string     `json:"error_info"`
	Result    UserResult `json:"result"`
}
