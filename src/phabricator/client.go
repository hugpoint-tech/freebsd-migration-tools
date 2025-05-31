package phabricator

type PhabClient struct {
	token string
	url   string
}

func NewPhabClient() PhabClient {
	// token, ok := os.LookupEnv("PHABRICATOR_TOKEN")
	// if !ok {
	// 	panic("PHABRICATOR_TOKEN is not set")
	// }
	return PhabClient{
		// token: token,

		token: "",
		url:   "https://reviews.freebsd.org/api/",
	}
}
