package main

import (
	"fmt"
	"sort"
)

func isPermutation(x, y string) bool {
	// Build two array of runes
	var runex []rune
	var runey []rune

	for _, x := range x {
		runex = append(runex, x)
	}

	for _, y := range y {
		runey = append(runey, y)
	}

	// If the length differs- the two strings
	// can't be permutations of each other
	if len(runex) != len(runey) {
		return false
	}

	// Sort the two arrays
	sort.Slice(runex, func(i, j int) bool {
		return runex[i] < runex[j]
	})

	sort.Slice(runey, func(i, j int) bool {
		return runey[i] < runey[j]
	})

	fmt.Println(runex)
	fmt.Println(runey)

	// Check to see if each element tallies
	// in the two arrays
	for i := range runex {
		if runex[i] != runey[i] {
			return false
		}
	}
	return true
}

func isPermutationMaps(x, y string) bool {
	freqMapx := make(map[rune]int)
	freqMapy := make(map[rune]int)

	for _, char := range x {
		freqMapx[char]++
	}

	for _, char := range y {
		freqMapy[char]++
	}

	fmt.Println(freqMapx)
	fmt.Println(freqMapy)
	// return reflect.DeepEqual(freqMapx, freqMapy)

	if len(freqMapx) != len(freqMapy) {
		return false
	}

	for ind, elemx := range freqMapx {
		elemy, ok := freqMapx[ind]
		if !ok || elemx != elemy {
			return false
		}
	}
	return true
}
func main() {
	fmt.Println(isPermutation("dog", "god"))
	fmt.Println(isPermutation("dogs", "god"))
	fmt.Println(isPermutationMaps("dogs", "god"))
	fmt.Println(isPermutationMaps("dogs", "god"))
}
