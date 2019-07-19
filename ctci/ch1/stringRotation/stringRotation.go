package main

import (
	"fmt"
	"strings"
)

func isSubstring(x, y string) bool {
	if strings.Contains(x+x, y) {
		return true
	} else {
		return false
	}
}

func main() {
	fmt.Println(isSubstring("waterbottle", "erbottlewat"))
	fmt.Println(isSubstring("cat", "dog"))
}
