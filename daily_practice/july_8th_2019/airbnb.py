import math

def binary_search_iterative(lst, num):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) / 2
        if num == lst[mid]:
            return mid
        elif num < lst[mid]:
            high = mid - 1
        elif num > lst[mid]:
            low = mid + 1
    return -1

def minimumCandiesPerHour(candyPiles, numHours):
    # Write your code here
    low, high = 1, max(candyPiles)
    while low <= high:
        mid = (low + high) / 2

        sum = 0
        for candies in candyPiles:
            sum += math.ceil(float(candies) / mid)
        if int(sum) == numHours:
            return mid

        if int(sum) < numHours:
            high = mid - 1
        elif int(sum) > numHours:
            low = mid + 1
    return -1


# def minimumCandiesPerHour(candyPiles, numHours):
#     # Write your code here
#
#     # i represents potential candies per hour
#     # we test all numbers between 1 and the max in candyPiles
#
#     for i in range(1, max(candyPiles)):
#         sum = 0
#         for candies in candyPiles:
#             sum += math.ceil(float(candies) / i)
#         if int(sum) == numHours:
#             return i

print minimumCandiesPerHour([4, 9, 11, 17], 8)
