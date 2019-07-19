def ran_check(num, low, high):
    if num >= low and num <= high:
        return True
    return False

print (ran_check(5, 2, 7))
print (ran_check(10, 2, 7))

def up_low(s):
    lower_count, upper_count = 0, 0
    for char in s:
        if char.islower():
            lower_count += 1
        if char.isupper():
            upper_count += 1
    return upper_count, lower_count

print (up_low('Hello Mr. Rogers, how are you this fine Tuesday?'))

def unique_list(lst):
    final_lst = []
    for elem in lst:
        if elem not in final_lst:
            final_lst.append(elem)
    return final_lst

print (unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

def multiply(nums):
    prod = 1
    for num in nums:
        prod *= num
    return prod

print (multiply([1, 2, 3, -4]))

def palindrome(s):
    return s == s[::-1]

print (palindrome('helleh'))

import string
def ispangram(str1, alphabet=string.ascii_lowercase):
    return set(str1.lower()) <= set(alphabet)

ispangram("The quick brown fox jumps over the lazy dog")
