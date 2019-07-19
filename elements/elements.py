import math

def list_squared(m, n):
    final_arr = []

    # for every number between m and n- find all its divisors-
    # sum the squares of all its divisors- take the square root of this
    # sum and check if it's an integer- if so add the number
    # and the sum squared of its divisors to an internal array
    for num in range(m, n + 1):
        # divisors
        divisors = [i for i in range(1, num + 1) if num % i == 0]

        # sums of the squares of divisors, sqrt of the sum
        sum_squared = sum(map(lambda x: x**2, divisors))
        sqrt_sum = math.sqrt(sum_squared)

        # check if the sqrt sum is an integer
        if sqrt_sum.is_integer():
            final_arr.append([num, sum_squared])
    return (final_arr)

print (list_squared(1, 250))


# Divisors of 42 are : 1, 2, 3, 6, 7, 14, 21, 42. These divisors squared are: 1, 4, 9, 36, 49, 196, 441, 1764. The sum of the squared divisors is 2500 which is 50 * 50, a square!
#
# Given two integers m, n (1 <= m <= n) we want to find all integers between m and n whose sum of squared divisors is itself a square. 42 is such a number.
#
# The result will be an array of arrays or of tuples (in C an array of Pair) or a string, each subarray having two elements, first the number whose squared divisors is a square and then the sum of the squared divisors.
#
# #Examples:
#
# list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
# list_squared(42, 250) --> [[42, 2500], [246, 84100]]
# The form of the examples may change according to the language, see Example Tests: for more details.

CACHE = {}

# the reason this works is that numbers
# share divisors in which case- we don't want to be recomputing
# the divisor sum for the same numbes repeatedly
def squared_cache(number):
    # if a number is not in the cache- compute its divisor sum
    # and store it in the cache
    if number not in CACHE:
        # pull all the divisors for a given number
        divisors = [x for x in range(1, number + 1) if number % x == 0]
        # cache a number to its divisor sum
        CACHE[number] = sum([x * x for x in divisors])
        return CACHE[number]

    # otherwise return the cache of the number
    return CACHE[number]


def list_squared(m, n):
    ret = []

    # go through every number from m to n- retrieve its squared
    # sum- check if the squared sum when square rooted is an
    # integer and if so append the number and divisor sum to ret
    for number in range(m, n + 1):
        divisors_sum = squared_cache(number)
        if (divisors_sum ** 0.5).is_integer():
            ret.append([number, divisors_sum])

    return ret
