# -*- coding: utf-8 -*-
# https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html
# - Know if a value is present in a list for more than half of the elements
# in that list

# Fault-tolerant computing- multiple redundant computations nad verify that
# a majority of results agree

# Sort the list- if there is a majority value it mut now be the middle
# run another pass through the list and count it's frequency

# O(1) extra space and O(n) time- 2 pases
# over the input list

# first pass- generate a single candidate value- majority value
# if there is a majority

# second pass counts the frequency of that value to confirm

# first pass- need candidate value- set to value, count set to 0

# each element examine count- if count is equal to 0- set candidate to value
# at the current element

# compare the element's value to current candidate value- same increment count
# by 1- different- decrement count by 1

# candidate = 0
# count = 0
# for value in input:
#   if count == 0:
#     candidate = value
#   if candidate == value:
#     count += 1
#   else:
#     count -= 1
# candidate will be majority if a majority value exists, O(n) pass
# to verify that the candidate is a majority element


# First, consider a list where the first element is not the majority value, for example this list with majority value 0:
#
# [5, 5, 0, 0, 0, 5, 0, 0, 5]

# processing the first element- aign 5 to candidate and 1
# to count
# 5 is not hte majority- at some point algorithm will find another
# value to pair with every 5 we've seen so far- count will drop to 0
# before the last element in the list- occurs at the 4th element

# [5, 5, 0, 0...]
# [1, 2, 1, 0...]
# count returns to 0- consumed same # of 5's as other elements
# if all elements were the majority element- consumed 2 majority and 2 non-majority
# largest # of majority elements consumed- majority
# must be a majority of the remainder of the input lit
# some of the other element were not majority elements this would be more true
# first element was a majority element and count drops to 0
# the majority element is still the majority of the remainder input list
# consumed equal # of majority and non majority elements

# demonstrates range of elements from time candidate is first assigned to when
# count drops to 0 can be discarded from the input without affecting the final
# result of the first pass

# repeat this over and over again discarding ranges that prefix our input until
# we find a range that is a suffix of our input where count never drops to 0

# input list suffix- count never drops to 0- must have more values than equal
# the first element than values that do no

# first element must be the majority of that list- only possible candidate
# for the majority of the full input list

# two
from collections import Counter

def majorityElement(arr):
    my_counter = Counter(arr)
    return [num for num, val in my_counter.items() if val > len(arr) / 3]

print majorityElement([1,1,1,3,3,2,2,2])
print majorityElement([3, 2, 3])

def majorityElement(self, nums, k):
    ctr = collections.Counter()
    for n in nums:
        ctr[n] += 1
        if len(ctr) == k:
            ctr -= collections.Counter(set(ctr))
    ctr = collections.Counter(n for n in nums if n in ctr)
    return [n for n in ctr if ctr[n] > len(nums)/k]

# @param {integer[]} nums
# @return {integer[]}
# def majorityElement(self, nums):
#     if not nums:
#         return []
#     count1, count2, candidate1, candidate2 = 0, 0, 0, 1
#     for n in nums:
#         if n == candidate1:
#             count1 += 1
#         elif n == candidate2:
#             count2 += 1
#         elif count1 == 0:
#             candidate1, count1 = n, 1
#         elif count2 == 0:
#             candidate2, count2 = n, 1
#         else:
#             count1, count2 = count1 - 1, count2 - 1
#     return [n for n in (candidate1, candidate2)
#                     if nums.count(n) > len(nums) // 3]
