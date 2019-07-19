package main

import (
	"fmt"
	"unicode"
)

func isPalindrome(x string) bool {
	freqMap := make(map[rune]int)
	for _, char := range x {
		if unicode.IsSpace(char) {
			continue
		} else {
			freqMap[unicode.ToLower(char)]++
		}
	}

	oddCount := 0
	for _, val := range freqMap {
		if val%2 == 1 {
			oddCount += 1
		}
		if oddCount > 1 {
			return false
		}
	}
	return true
}

// So now instead of going through the frequency map
// keep track of an oddCount as you're building the map

// To take an example Taco Coa
// T -> 1, a -> 2, c -> 3, o -> 4, ignore whitespace, C -> 3
// o -> 2, a -> 1

// Before the whitespace chars (in this case) freq map is odd for
// each char, so we increment oddCount, after whitespace freq count for
// each character is even and so we decrement oddCount, if oddCount is
// 0 or 1- we have ourselves a permutation of a palindrome

func isPalindromeCompact(x string) bool {
	freqMap := make(map[rune]int)
	oddCount := 0
	for _, char := range x {
		if unicode.IsSpace(char) {
			continue
		} else {
			freqMap[unicode.ToLower(char)]++
			if freqMap[unicode.ToLower(char)]%2 == 1 {
				oddCount += 1
			} else {
				oddCount -= 1
			}
		}
	}

	if oddCount == 0 || oddCount == 1 {
		return true
	} else {
		return false
	}
}

func main() {
	fmt.Println(isPalindrome("Taco Coa"))
	fmt.Println(isPalindrome("tactcoapapa"))

	fmt.Println(isPalindromeCompact("Taco Coa"))
	fmt.Println(isPalindromeCompact("tactcoapapa"))
}
