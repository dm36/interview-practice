from collections import Counter
# can only have one character with an odd frequency

# def permutation_palindrome(string):
#     freq_map = Counter(string)
#     odd_count = 0
#
#     for char, count in freq_map.items():
#         if count % 2 == 1:
#             odd_count += 1
#
#     return odd_count <= 1
#
# def permutation_palindrome(string):
#     freq_map = {}
#     for char in string:
#         if char not in freq_map:
#             freq_map[char] = 1
#         else:
#             freq_map[char] += 1
#
#     return len([char for char, freq in freq_map.items() if freq % 2 == 1]) <= 1

def permutation_palindrome(string):
    unpaired_chars = set()
    for char in string:
        if char not in unpaired_chars:
            unpaired_chars.add(char)
        elif char in unpaired_chars:
            unpaired_chars.remove(char)
    return len(unpaired_chars) <= 1

# print (permutation_palindrome("racecar"))
print (permutation_palindrome("dog"))
