def toJadenCase(string):
	upper_case_arr = [string[0].upper() + string[1:] for string in string.split(" ")]
	return ' '.join(upper_case_arr)
