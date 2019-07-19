import collections

def duplicate_count(text):
	freq_map = collections.defaultdict(int)
	for char in text:
		freq_map[char.lower()] += 1

	return len([key for key, val in freq_map.items() if val > 1])
