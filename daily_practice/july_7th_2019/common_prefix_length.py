# generate all suffixes of the string

# get the longest prefix match
#
# def commonPrefix(my_string):
#     suffixes = []
#     count = 0
#     for i in range(len(my_string)):
#         suffixes.append(my_string[i:])
#
#     for suffix in suffixes:
#         count += longest_prefix_match(my_string, suffix)
#
#     return [count]
#
#
# def longest_prefix_match(my_string, suffix):
#     i, j = 0, 0
#     count = 0
#
#     while i < len(my_string) and j < len(suffix) and my_string[i] == suffix[j]:
#         i += 1
#         j += 1
#         count += 1
#
#     return count
# def commonPrefix(my_string):
#     suffixes = []
#     count = 0
#     for i in range(len(my_string)):
#         suffixes.append(my_string[i:])
#
#     for suffix in suffixes:
#         count += longest_prefix_match(my_string, suffix)
#
#     return count
#
#
# def longest_prefix_match(my_string, suffix):
#     i, j = 0, 0
#     count = 0
#
#     while i < len(my_string) and j < len(suffix) and my_string[i] == suffix[j]:
#         i += 1
#         j += 1
#         count += 1
#
#     return count

# print longest_prefix_match("ababaa", "babaa")

#!/bin/python

# import math
# import os
# import random
# import re
# import sys



#
# Complete the 'commonPrefix' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY inputs as parameter.
#

# def commonPrefix(my_string):
#     suffixes = []
#     final_arr = []
#     count = 0
#     my_string = my_string[0]
#     for i in range(len(my_string)):
#         suffixes.append(my_string[i:])
#     print suffixes
#     for suffix in suffixes:
#         count += longest_prefix_match(my_string, suffix)
#
#     return [count]
#
#
# def longest_prefix_match(my_string, suffix):
#     i, j = 0, 0
#     count = 0
#
#     while i < len(my_string) and j < len(suffix) and my_string[i] == suffix[j]:
#         i += 1
#         j += 1
#         count += 1
#
#     return count
#
#
# if __name__ == '__main__':
#

def longestCommonPrefix(strs):
    longest_pre = ""
    if not strs: return longest_pre
    shortest_str = min(strs, key=len)
    for i in range(len(shortest_str)):
        print x.startswith(shortest_str[:i+1])
        # if all([x.startswith(shortest_str[:i+1]) for x in strs]):
        #     longest_pre = shortest_str[:i+1]
        # else:
        #     break
    return longest_pre

print longestCommonPrefix(["flower", "flow", "flight"])
# print commonPrefix("ababaa")
# print commonPrefix("aa")
