# List of integers in the range 1...n
# list has a length of n + 1
# find an integer that appears more than once in the list

# check every element against every other element
# and if the two elements don't have the same index and are =
# we have our duplicate
# def find_duplicate(lst):
#     for i in range(len(lst)):
#         for j in range(len(lst)):
#             if i != j and lst[i] == lst[j]:
#                 return lst[i]

# sort list and check adjacent elements for a duplicate
# upper bound is len(lst) - 1 because otherwise we'd get an index
# out of bounds error
# def find_duplicate(lst):
#     lst.sort()
#     for i in range(len(lst)-1):
#         if lst[i] == lst[i+1]:
#             return lst[i]

# use Counter- find the most common element- and return that
# def find_duplicate(lst):
#     nums_count = Counter(lst)
#     return nums_count.most_common(1)

# build a set- and if an element is already in our set
# return it
# def find_duplicate(lst):
#     nums = set()
#     for num in lst:
#         if num in nums:
#             return num
#         else:
#             nums.add(num)

# binary search approach:
# duplicate can either be in (0, n/2) or (n/2 + 1, n)

# how do we know where it is?

# compare the number of elements that are actually in that range to the
# size of the range to know where to go

# more specifically:

# low and high indices- initialized first to 0 and the length of the list
# find the midpoint index ((low + high) / 2)
# (low, midpoint), (midpoint + 1, high) are our two ranges
# go through the list and count the number of elements between
# low and midpoint (i.e. by comparing every element to low and midpoint)
# and if that's greater than midpoint - low + 1
# we're going to the left to find our duplicate!
# otherwise we goin' right
# and for going left => set low, high to be low, midpoint
# you also got to do this low ceiling, low floor
# can't just keep a low, mid and a high

# def find_duplicate(list, low, high):
#     while low < high:
#         mid = (low + high) / 2
#
#         left_range_count = 0
#         for item in list:
#             if low <= item <= high:
#                 left_range_count += 1
#
#         left_range_size = mid - low + 1
#
#         if left_range_count > left_range_size:
#             low, high = low, mid - 1
#         else:
#             low, high = mid + 1, high
#     return low

def find_repeat(the_list):
    floor = 1
    ceiling = len(the_list) - 1

    while floor < ceiling:
        # Divide our range 1..n into an upper range and lower range
        # (such that they don't overlap)
        # Lower range is floor..midpoint
        # Upper range is midpoint+1..ceiling
        mid = floor + ((ceiling - floor) / 2)
        # lower_range_floor, lower_range_ceiling = floor, midpoint
        # upper_range_floor, upper_range_ceiling = midpoint+1, ceiling

        # Count number of items in lower range
        items_in_lower_range = 0
        for item in the_list:
            # Is it in the lower range?
            # if item >= lower_range_floor and item <= lower_range_ceiling:
            #     items_in_lower_range += 1
            if item >= floor and item <= ceiling:
                items_in_lower_range += 1

        distinct_possible_integers_in_lower_range = (
            ceiling
            - floor
            + 1
        )
        if items_in_lower_range > distinct_possible_integers_in_lower_range:
            # There must be a duplicate in the lower range
            # so use the same approach iteratively on that range
            floor, ceiling = floor, mid
        else:
            # There must be a duplicate in the upper range
            # so use the same approach iteratively on that range
            floor, ceiling = mid + 1, ceiling

    # Floor and ceiling have converged
    # We found a number that repeats!
    return floor


list = [1, 2, 3, 4, 4]
print find_repeat(list)
