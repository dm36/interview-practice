# https://leetcode.com/problems/rotate-string/solution/


# We are given two strings, A and B.
#
# A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.
#
# Example 1:
# Input: A = 'abcde', B = 'cdeab'
# Output: true
#
# Example 2:
# Input: A = 'abcde', B = 'abced'
# Output: false
# Note:
#
# A and B will have length at most 100.

def shift_string(str):
    return str[1:] + str[0]

def rotateString(A, B):
    my_len = len(A)
    while my_len:
        A = shift_string(A)
        if A == B:
            return True
        my_len -= 1
    return False

# class Solution(object):
#     def rotateString(self, A, B):
#         """
#         :type A: str
#         :type B: str
#         :rtype: bool
#         """
#         if A == B:
#             return True
#
#         my_len = len(A)
#         while my_len:
#             A = shift_string(A)
#             if A == B:
#                 return True
#             my_len -= 1
#         return False
#
# def shift_string(my_str):
#     return my_str[1:] + my_str[0]

print shift_string("abcde")
print rotateString('abcde', 'cdeab')
print rotateString('abcde', 'abced')
