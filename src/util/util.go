package util

import (
	"fmt"
	"os"
)

func Fatal(msg string) {
	_, _ = fmt.Fprintf(os.Stderr, "fatal: %s\n", msg)
	os.Exit(1)
}

func Fatalf(format string, args ...any) {
	formatString := fmt.Sprintf("fatal: %s\n", format)
	_, _ = fmt.Fprintf(os.Stderr, formatString, args...)
	os.Exit(1)
}

func CheckFatal(msg string, e error, args ...any) {
	if e != nil {
		_, _ = fmt.Fprintf(os.Stderr, "fatal: %s %s\n", msg, e)
		os.Exit(1)
	}
}
