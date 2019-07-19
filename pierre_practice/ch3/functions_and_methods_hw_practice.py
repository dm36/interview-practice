import math
from collections import Counter

def vol(rad):
    return 4/3 * math.pi * (rad**3)

print (vol(2))

def ran_check(num, low, high):
    if num >= low and num <= high:
        return "{} is in the range between {} and {}".format(num, low, high)
    else:
        return "{} is not in the range between {} and {}".format(num, low, high)

# def ran_check(num,low,high):
#     #Check if num is between low and high (including low and high)
#     if num in range(low,high+1):
#         print('{} is in the range between {} and {}'.format(num,low,high))
#     else:
#         print('The number is outside the range.')

def ran_bool(num, low, high):
    return num >= low and num <= high

# def ran_bool(num,low,high):
#     return num in range(low,high+1)
print (ran_check(5, 2, 7))

#
# def up_low(s):
#     d={"upper":0, "lower":0}
#     for c in s:
#         if c.isupper():
#             d["upper"]+=1
#         elif c.islower():
#             d["lower"]+=1
#         else:
#             pass
#     print("Original String : ", s)
#     print("No. of Upper case characters : ", d["upper"])
#     print("No. of Lower case Characters : ", d["lower"])

def up_low(s):
    return len([s for char in s if char.isupper()]), len([s for char in s if char.islower()])

print (up_low('Hello Mr. Rogers, how are you this fine Tuesday?'))

# def unique_list(lst):
#     # Also possible to use list(set())
#     x = []
#     for a in lst:
#         if a not in x:
#             x.append(a)
#     return x

def unique_lst(lst):
    return list(set(lst))

print (unique_lst([1,1,1,1,2,2,3,3,3,3,4,5]))

def multiply(numbers):
    prod = 1
    for num in numbers:
        prod *= num
    return prod

print (multiply([1, 2, 3, -4]))

def palindrome(s):
    return s == s[::-1]

print (palindrome("helleh"))

# https://docs.python.org/3/library/string.html
import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    chars = [char.lower() for char in str1 if not char.isspace()]
    return ''.join(sorted(list(set(chars)))) == alphabet

# import string
#
# def ispangram(str1, alphabet=string.ascii_lowercase):
#     alphaset = set(alphabet)
#     return alphaset <= set(str1.lower())

print (ispangram("The quick brown fox jumps over the lazy dog"))
print (ispangram("The quick"))
