package main

import "fmt"
import "sort"

func is_unique(x string) bool {
	freq_map := make(map[rune]int)
	for _, char := range x {
		freq_map[char] += 1
		if freq_map[char] > 1 {
			return false
		}
	}
	return true
}

func is_unique_compare(x string) bool {
	for i, elem1 := range x {
		for j, elem2 := range x {
			if i != j && elem1 == elem2 {
				return false
			}
		}
	}
	return true
}

func is_unique_sort(x string) bool {
	// Create an array of runes
	var r []rune
	for _, rune := range x {
		r = append(r, rune)
	}

	// fmt.Println(r)
	// Sort the array of runes
	sort.Slice(r, func(i, j int) bool {
		return r[i] < r[j]
	})

	// fmt.Println(r)

	// Convert the array of runes to a string
	sorted_string := string(r)
	// fmt.Println(sorted_string)

	for i := 0; i < len(sorted_string)-1; i++ {
		if sorted_string[i] == sorted_string[i+1] {
			return false
		}
	}

	return true
}

func main() {
	fmt.Println("Is unique: ")
	fmt.Println(is_unique("swag"))
	fmt.Println(is_unique("swags"))
	fmt.Println(is_unique("dogd"))
	fmt.Println()

	fmt.Println("Is unique sort: ")
	fmt.Println(is_unique_sort("swag"))
	fmt.Println(is_unique_sort("swags"))
	fmt.Println(is_unique_sort("dogd"))
	fmt.Println()

	fmt.Println("Is unique compare: ")
	fmt.Println(is_unique_compare("swag"))
	fmt.Println(is_unique_compare("swags"))
	fmt.Println(is_unique_compare("dogd"))
	fmt.Println()

}
