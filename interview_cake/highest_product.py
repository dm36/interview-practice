from itertools import combinations

# build all combinations of 3 integers
# compute each combination's product and return the
# largest product

# runtime is O(nC3)
def highest_product_comb(nums):
    max_prod = -float("inf")
    for comb in combinations(nums, 3):
        prod = comb[0] * comb[1] * comb[2]
        max_prod = max(prod, max_prod)
    return max_prod

# O(n^3)- return the max observed product of integers
# at unique indices
def highest_product_inefficient(nums):
    max_prod = -float("inf")
    for i in range(len(nums)):
        for j in range(len(nums)):
            for k in range(len(nums)):
                if i != j != k:
                    max_prod = max(max_prod, nums[i] * nums[j] * nums[k])

    return max_prod


# sort the array and pick the max of:
# 1) the three largest numbers
# 2) the two smallest number and the largest number
# O (nlogn)
def highest_product_sort(nums):
    nums.sort()
    max_positive = nums[-1] * nums[-2] * nums[-3]
    max_negative = nums[0] * nums[1] * nums[-1]

    return max(max_positive, max_negative)

# the highest product of 3 is either:
# 1) the highest product of 3 observed thus far
# 2) the current * times the highest product of 2 numbers observed so far
# 3) the current * the lowest product of 2 numbers observed so far (if current is -)

# the highest product of 2 is either:
# 1) the highest product of 2 observed so far
# 2) current * the highest number observed so far (if current is +)
# 3) current * the lowest number observed so far (if current is -)

# the highest number so far
# is either current or the highest number observed so far

# the lowest number so far
# is either current or the lowest number observed so far
def highest_product_greedy(nums):
    # highest_product_of_three = -float("inf")
    # highest_product_of_two = -float("inf")
    # lowest_product_of_two = float("inf")
    # highest_number = -float("inf")
    # lowest_number = float("inf")

    # any other way we can initialize these vars before the loop?
    highest_product_of_three = nums[0] * nums[1] * nums[2]
    highest_product_of_two = nums[0] * nums[1]
    lowest_product_of_two = nums[0] * nums[1]
    highest_number = max(nums[0], nums[1])
    lowest_number = min(nums[0], nums[1])

    # if you don't do it in this order- you might end up multiplying
    # current by itself to get a new highest product of 2
    for i in range(2, len(nums)):
        highest_product_of_three = max(highest_product_of_three,
        nums[i] * lowest_product_of_two, nums[i] * highest_product_of_two)

        highest_product_of_two = max(highest_product_of_two, nums[i] * highest_number,
        nums[i] * lowest_number)
        highest_number = max(nums[i], highest_number)
        lowest_number = min(nums[i], lowest_number)
    return highest_product_of_three


# print highest_product_comb([-10, -10, 1, 3, 2])
# print highest_product_inefficient([-10, -10, 1, 3, 2])
# print highest_product_sort([-10, -10, 1, 3, 2])
print highest_product_greedy([-10, -10, 1, 3, 2])
