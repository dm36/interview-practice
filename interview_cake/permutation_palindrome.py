from collections import Counter
from collections import defaultdict
from itertools import permutations
import sys

# https://docs.python.org/2/library/collections.html#collections.Counter

# can only have at most one odd count with the
# chars of a string

# using counter
def permutation_palindrome(str):
    counter = Counter(str)
    odd_count = 0

    for key, val in counter.items():
        if val % 2 == 1:
            odd_count += 1
            if odd_count > 1:
                return False

    return True

# using hash maps no counter

# O(n) time and O(n) space
def another_permutation_palindrome(str):
    hash_map = defaultdict(int)

    for char in str:
        hash_map[char] += 1

    odd_count = 0
    for val in hash_map.values():
        if val % 2 == 1:
            odd_count += 1
            if odd_count > 1:
                return False
    return True

# using permutations- this is by far the least efficient

# n! permutations of a n-length string- have to go through
# all n chars so O(n! * n)
def another_another_permutation_palindrome(str):
    for p in permutations(str):
        potential_pali = ''.join(p)
        if potential_pali == potential_pali[::-1]:
            return True
    return False

# O(n) time, O(k) space- we can only have the # of unique
# chars in a set at a given point in time
def has_palindrome_permutation(the_string):
    # Track characters we've seen an odd number of times
    unpaired_characters = set()

    for char in the_string:
        if char in unpaired_characters:
            unpaired_characters.remove(char)
        else:
            unpaired_characters.add(char)

    # The string has a palindrome permutation if it
    # has one or zero characters without a pair
    return len(unpaired_characters) <= 1


print permutation_palindrome("civic")
print permutation_palindrome("ivicc")
print permutation_palindrome("civil")
print permutation_palindrome("livci")
print

print another_permutation_palindrome("civic")
print another_permutation_palindrome("ivicc")
print another_permutation_palindrome("civil")
print another_permutation_palindrome("livci")
print

print another_another_permutation_palindrome("civic")
print another_another_permutation_palindrome("ivicc")
print another_another_permutation_palindrome("civil")
print another_another_permutation_palindrome("livci")
print

# names of loaded modules
# print sys.modules.keys()
# print itertools
# print defaultdict
