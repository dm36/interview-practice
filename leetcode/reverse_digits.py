import re

# https://stackoverflow.com/questions/13142347/how-to-remove-leading-and-trailing-zeros-in-a-string-python
# class Solution:
#     def reverse(self, x: int) -> int:
#         if x == 0:
#             return 0
#
#         x = str(x)
#         minus_flag = False
#
#         if x[0] == '-':
#             minus_flag = True
#             x = x[1:]
#
#         x = x.rstrip("0")
#
#         if minus_flag == True:
#             new_int = int("-" + x[::-1])
#         else:
#             new_int = int(x[::-1])
#
#         if new_int >= 2**31 - 1 or new_int <= -2**31:
#             return 0
#         else:
#             return new_int

# https://www.geeksforgeeks.org/python-cmp-function/
# def reverse(x):
#     # extrapolates the - sign by comparing the number with 0
#     # if it is greater returns 1, if it is less returns -1
#     s = cmp(x, 0)
#
#     # multiply the number by its sign -> convert to a string ->
#     # reverse the result and cast to an integer
#     r = int(`s*x`[::-1])
#
#     # multiply the - sign by the number by whether or not
#     # the number is less than 2**31 (to account for overflow)
#     return s*r * (r < 2**31)

# def reverse(x):
#     s=cmp(x,0);r=int(`s*x`[::-1]);return(r<2**31)*s*r
#
# def reverse(x):
#     # - if the provided number is negative, positive
#     # if the # is +
#     s = (x > 0) - (x < 0)
#
#     # convert to a string reverse -> convert back to
#     # an integer
#     r = int(str(x*s)[::-1])
#     return s*r * (r < 2**31)
#
def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    # if x is > 0 -> 0 so 1
    # if x is < 0 -> 1 so -1
    sign = [1,-1][x < 0]

    # take the absolute value -> convert to a string ->
    # reverse the string -> cast it as an integer
    # and multiply it by the sign
    rst = sign * int(str(abs(x))[::-1])

    # account for overflow
    return rst if -(2**31)-1 < rst < 2**31 else 0

print (reverse(-123))
# print reverse_digits(1534236469)
#
#
# print reverse_digits(1203)
# print reverse_digits(-123)
# print reverse_digits(120)

# print reverse_digits("1203")
# print reverse_digits("-123")
# print reverse_digits("120")
