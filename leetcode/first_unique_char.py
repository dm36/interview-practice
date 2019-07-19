# enumerate every index and character in the string and
# return the first index for which the character count is 1

# build a frequency map of every character to its count- iterate through the
# string and check that frequency map to find the count where it's equal to 1
def find_first_non_repeating_char(s):
    for ind, char in enumerate(s):
        if s.count(char) == 1:
            return ind

print find_first_non_repeating_char("leetcode")

# O(n) runtime- go through each character and access it from counter
# accessing is O(1) amortized, O(n)

# lookups involve invoking the hash function to find the index and then
# traversing through the internal linked list to find the appropriate node
from collections import Counter
def find_first_non_repeating_char(s):
    freq_map = Counter(s)
    for i in range(len(s)):
        if freq_map[s[i]] == 1:
            return i

print (find_first_non_repeating_char("leetcode"))

from collections import Counter
def find_first_non_repeating_char(s):
    sorted_s = ''.join(sorted(s))
    for i in range(1, len(sorted_s)):
        if sorted_s[i] == sorted_s[i+1]:
            char = 

print (find_first_non_repeating_char("leetcode"))
