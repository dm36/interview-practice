from collections import Counter
def first_non_repeating_letter(string):
	# string -> lower-case, build a frequency map
	# of the string's lower case chars
	lower_case_string = string.lower()
	count = Counter(lower_case_string)

	# Need to index into our map by converting a character
	# to lower-case (as that is how our frequency map is represented)

	# Find the first character that has a frequency count of 1
	for char in string:
		if count[char.lower()] == 1:
			return char

	# Return empty string if the string has all repeating chars
	return ""
