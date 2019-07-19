using System;

// To execute C#, please define "static void Main" on a class
// named Solution.

class Solution
{
    static void Main(string[] args)
    {
        for (var i = 0; i < 5; i++)
        {
            Console.WriteLine("Hello, World");
        }
    }
}

he said, you should ow
/*
Your previous Python 3 content is preserved below:

# def say_hello():
#     print('Hello, World')

# for i in range(5):
#     say_hello()


# Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

# Note:
# The length of num is less than 10002 and will be ≥ k.
# The given num does not contain any leading zero.
# Example 1:

# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
# Example 2:

#     ignore this edge case - leading zero removal
# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
# Example 3:

#     ignore this edge case - let us work on main problem first
# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with nothing which is 0.


# class Solution:
#     def removeKdigits(self, num: str, k: int) -> str:


# 3CN = O(n!)
# brute force solution- pick all combinations of 3 digits from the input
# remove each combination from the input and get the resulting number
# then take the minimum of all these numbers

# 1432219

# assign every digit its numerical value
# (looking at this in reverse)
# give it a priority

# 9 = 9
# 1 = 10
# 2 = 200
# 2 = 2000
# 3 = 30,000
# 4 = 400,000
# 1 = 1,000,000

# 1432219

# go through every digit- remove it and check what the minimum could be with
# the remaining digits- until we have removed k digits
# once k is 0- return that number that we have

# [1, 4, 3, 2, 2, 1, 9]
# choose to remove the 1, min(removeKDigits(432219, k - 1)
# choose to remove the 4, min(removeKDigits(132219, k - 1))

# 1432219 as your input
# n is the number of digits in your number

# [1, 4, 3, 2, 2, 1, 9]
# delete the 1, [4, 3, 2, 2, 1, 9]
# delete the 4, [1, 3, 2, 2, 1, 9]

# left with [4, 3, 2, 2, 1, 9]


# 1432219
# either you delete the 1 or not
# i is an index that is initialized to the number of digits in the input
# delete the 1 min(432219, k - 1, i + 1) or min(1432219, k, i)


# first case is if we choose to remove that digit
# slice it out, increment i, decrement k

# second case
# is if we chooose to keep that digit, nums stays the same
# i increments by 1 (we're moving over a digit, and k remains the same
# because we haven't removed a digit)
import pdb

def convert_array_to_num(array):
    for i in range(len(array)):
        array[i] = int(array[i])

    num = 0
    for i in range(len(array) - 1, -1, -1):
        num += array[i] * 10 ** (len(array) - i - 1)
    return num

def helper_remove_k_digits(nums, i, k):
    # we've removed k digits, we should return the number now
    if k == 0 or i > len(nums):
        print (convert_array_to_num(nums))
        return convert_array_to_num(nums)

    # trying to take the min of two arrays which doesn't make sense
    return min(helper_remove_k_digits(nums[1:], i, k - 1), helper_remove_k_digits(nums, i + 1, k))

def convert_num_to_array(num):
    return list(str(num))


def removeKDigits(num, k):
    i = 0
    # convert this number to an array
    nums = convert_num_to_array(num)

    # helper function which will return the minimum possible number!
    return helper_remove_k_digits(nums, i, k)

    1432219, 3 , keep 4
    ---- first 4 digits should be minimum digit in the first 4 digits, leftmost digit
    reserve three digits -
    O(n-k) * n -> O(n^2)

    pass - 60 minutes
   - stack O(N)

    2134, k = 2, minimum is 13

    2, push 2,
    1, compare 1 with top of stack 2, 2 > 1, argue that first digit 2 will not be candidate, why? 2x > 1y,
    remove 2 out of stack, k--, k = 1,
    push 1 into stack
    visit 3, 3 > 1,
    viist 4,
    1 -> 3 -> 4

    k = 1, remove any digit, top of stck , remove 4

    1-> 3


    he sai



print (removeKDigits(1432219, 3))

# # first iteration nums will have length 7
# # i will be 0

# removeKDigits(12, 3)

# linear runtime -> trie

# hash map to store numbers that you've seen before- and then
# don't
# if when you remove a digit you've seen the number before- don't recurse

# word-
 */
