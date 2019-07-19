# For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)
#
# Return the largest string X such that X divides str1 and X divides str2.
#
# Example 1:
#
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:
#
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:
#
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
#
#
# Note:
#
# 1 <= str1.length <= 1000
# 1 <= str2.length <= 1000
# str1[i] and str2[i] are English uppercase letters.

# from collections import Counter
#
# def gcdOfStrings(str1, str2):
#     l1, l2 = len(str1), len(str2)
#     if l2 > l1:
#         gcdOfStrings(str2, str1)
#
#     if l1 % l2 == 0:
#         count = l1 / l2
#         final_str = ""
#
#         while count:
#             final_str += str2
#             count -= 1
#
#         if final_str == str1:
#             return str2
#
#     if not set(Counter(str2).keys()).issubset(Counter(str1).keys()):
#         return ""
#     elif str1 not in str2 and str2 not in str1:
#         return ""

def gcdOfStrings(str1, str2):
    # if the two strings are equal (base case)
    # return the first string
    # otherwise return ''
    if len(str1) == len(str2):
        return str1 if str1==str2 else ''
    else:
        if len(str1) < len(str2):
            str1,str2 = str2,str1
        if str1[:len(str2)] == str2:
            return gcdOfStrings(str1[len(str2):],str2)
        else:
            return ''

# since ABAB and ABAB match
# would call gcd on "AB" and "ABAB"
# which would then call gcd on "AB", "AB"
# which would return "AB"
gcdOfStrings("ABABAB", "ABAB")

#
# str1 = "ABCABC"
# str2 = "ABC"
# print (gcdOfStrings(str1, str2))
#
# str1 = "ABABAB"
# str2 = "ABAB"
# print (gcdOfStrings(str1, str2))
#
# str1 = "LEET"
# str2 = "CODE"
# print (gcdOfStrings(str1, str2))
