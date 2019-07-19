def reverse_digits(num):
    # sign is 1 if numbers is + and -1 if number is 0
    sign = cmp(num, 0)

    # multiply the number by its sign (to remove the sign)
    # convert it to a string- remove all 0's from the right and reverse
    # the string and then cast it to an integer

    # and then multiply it by whether or not it is greater than 2**31 - 1
    result = sign * int((str(num * sign).rstrip('0')[::-1]))
    return 0 if result > 2**31 - 1 or result < -2**31 else result

print reverse_digits(1534236469)
print reverse_digits(-1230)
# print reverse_digits(123)
