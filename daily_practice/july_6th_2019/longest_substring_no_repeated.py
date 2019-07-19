# def generate_all_substrings(str):
#     all_substrings = []
#     for size in range(len(str) + 1, 0, -1):
#         for start_ind in range(len(str)):
#             if start_ind + size > len(str):
#                 break
#             all_substrings.append(str[start_ind : start_ind + size])
#     return all_substrings
#
# def longest_palindrome(str):
#     all_substrings = generate_all_substrings(str)
#     for substr in all_substrings:
#         if substr == substr[::-1]:
#             return substr
#     return -1
#
# print longest_palindrome("babad")
# print longest_palindrome("cbbd")

# Starts at each index and expands outwards
# as long as the string is still a palindrome and then returns
# the longest string across all such runs
def longestPalindrome(s):
    res = ""

    # update res string if length is longer

    for i in xrange(len(s)):
        # odd case, like "aba"
        tmp = helper(s, i, i)
        if len(tmp) > len(res):
            res = tmp
        # even case, like "abba"
        tmp = helper(s, i, i+1)
        if len(tmp) > len(res):
            res = tmp
    return res

# get the longest palindrome, l, r are the middle indexes
# from inner to outer
def helper(s, l, r):
    # as long as l is greater than 0 and r is less than the length of the string
    # and the left and right characters are equal- decrement l and increment r

    # return the string starting from the left index- and going to but
    # not including the right index

    # expanding outwards
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1; r += 1
    return s[l+1:r]

# def longestPalindrome(self, s):
#     """
#     :type s: str
#     :rtype: str
#     """
#
#     res = ""
#     for i in range(len(s)):
#         res = max(self.helper(s,i,i), self.helper(s,i,i+1), res, key=len)
#
#     return res
#
#
# def helper(self,s,l,r):
#
#     while 0<=l and r < len(s) and s[l]==s[r]:
#             l-=1; r+=1
#     return s[l+1:r]

print longestPalindrome("babad")
print longestPalindrome("cbbd")
