def helper_function(integers, even_or_odd):
	for integer in integers:
		if integer % 2 == even_or_odd:
			return integer

def find_outlier(integers):
    even = [integer for integer in integers if integer % 2 == 0]
    odds = [integer for integer in integers if integer % 2 == 1]
    even_or_odd = 1 if len(even) > len(odds) else 0
    return helper_function(integers, even_or_odd)
