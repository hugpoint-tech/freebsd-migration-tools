package bugzilla

type Bug struct {
	ActualTime          string   `json:"actual_time"`
	Alias               []string `json:"alias"`
	AssignedTo          string   `json:"assigned_to"`
	AssignedToDetail    User     `json:"assigned_to_detail"`
	Blocks              []int    `json:"blocks"`
	CC                  []string `json:"cc"`
	CCDetail            []User   `json:"cc_detail"`
	Classification      string   `json:"classification"`
	Component           string   `json:"component"`
	CreationTime        string   `json:"creation_time"`
	Creator             string   `json:"creator"`
	CreatorDetail       User     `json:"creator_detail"`
	Deadline            string   `json:"deadline"`
	DependsOn           []int    `json:"depends_on"`
	DupeOf              int      `json:"dupe_of"`
	EstimatedTime       string   `json:"estimated_time"`
	Flags               []Flag   `json:"flags"`
	Groups              []string `json:"groups"`
	ID                  int      `json:"id"`
	IsCCAccessible      bool     `json:"is_cc_accessible"`
	IsConfirmed         bool     `json:"is_confirmed"`
	IsOpen              bool     `json:"is_open"`
	IsCreatorAccessible bool     `json:"is_creator_accessible"`
	Keywords            []string `json:"keywords"`
	LastChangeTime      string   `json:"last_change_time"`
	OpSys               string   `json:"op_sys"`
	Platform            string   `json:"platform"`
	Priority            string   `json:"priority"`
	Product             string   `json:"product"`
	QAContact           string   `json:"qa_contact"`
	QAContactDetail     User     `json:"qa_contact_detail"`
	RemainingTime       string   `json:"remaining_time"`
	Resolution          string   `json:"resolution"`
	SeeAlso             []string `json:"see_also"`
	Severity            string   `json:"severity"`
	Status              string   `json:"status"`
	Summary             string   `json:"summary"`
	TargetMilestone     string   `json:"target_milestone"`
	UpdateToken         string   `json:"update_token"`
	URL                 string   `json:"url"`
	Version             string   `json:"version"`
	Whiteboard          string   `json:"whiteboard"`
}

type BugsResponse struct {
	Bugs []Bug `json:"bugs"`
}

type UsersResponse struct {
	Users []User `json:"users"`
}

type User struct {
	ID       int     `json:"id"`
	Email    string  `json:"email"`
	Name     string  `json:"name"`
	CanLogin bool    `json:"can_login"`
	RealName string  `json:"real_name"`
	Groups   []Group `json:"groups"`
}

type Group struct {
	ID          int    `json:"id"`
	Name        string `json:"name"`
	Description string `json:"description"`
}

type Flag struct {
	ID               int    `json:"id"`
	Name             string `json:"name"`
	TypeID           int    `json:"type_id"`
	CreationDate     string `json:"creation_date"`
	ModificationDate string `json:"modification_date"`
	Status           string `json:"status"`
	Setter           string `json:"setter"`
	Requestee        string `json:"requestee,omitempty"`
}

type Comment struct {
	ID           int    `json:"id"`
	BugID        int    `json:"bug_id"`
	AttachmentID int    `json:"attachment_id"`
	CreationTime string `json:"creation_time"`
	Creator      string `json:"creator"`
	Text         string `json:"text"`
}

type Attachment struct {
	ID           int    `json:"id"`
	BugID        int    `json:"bug_id"`
	CreationTime string `json:"creation_time"`
	Creator      string `json:"creator"`
	Summary      string `json:"summary"`
	Data         []byte `json:"data"`
}

type CommentsResponse struct {
	Bugs map[int]struct {
		Comments []Comment `json:"comments"`
	} `json:"bugs"`
}

type AttachmentsResponse struct {
	Bugs map[int][]Attachment `json:"bugs"`
}
