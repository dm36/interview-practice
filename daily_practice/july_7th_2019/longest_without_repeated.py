from collections import defaultdict
def lengthOfLongestSubstring(s):
    exist = defaultdict(int)
    i, maxLen = 0, 0

    # i is the starting pointer, j the ending pointer

    # as long as s[j] equals 1 => i.e.
    # we've seen this character before
    # map s[i] to 0, and increment i

    # map s[j] to 1 in the exists mapping and update
    # the max length observed thus far

    # also read page 19 of leetcode 50 most commmon...

    # use a simple table to store the characters
    # that have appeared

    # what happens when you find a repeated character?
    # if the string is abcdcedf- what happens
    # when you reach the second appearance of c

    # when you've found a repeated character- it means
    # that the current substring (excluding the
    # repeated char) is a potential max- so update
    # max if needed. means that repeated character
    # must have appeared before at an index i
    # where i < j

    # all substrings that start before at index i would
    # be less than current max- can safely start
    # to look for next substring with head which
    # starts exactly at index i + 1

    # think of exist as containing all
    # the characters that are in play for a potential
    # longest non-repeating substring

    for j in range(len(s)):
        while exist[s[j]] == 1:
            exist[s[i]] = 0
            i += 1
        exist[s[j]] = 1
        maxLen = max(j - i + 1, maxLen)
    return maxLen

# print lengthOfLongestSubstring("bbbbb")
print lengthOfLongestSubstring("abcabcbb")
