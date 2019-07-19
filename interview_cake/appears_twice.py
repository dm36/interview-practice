# take the length of the list (n) and subtract 1
# (n * n + 1) / 2 is the sum of numbers of 1 - n

# actual sum is sum of list

# take the difference

# to get concrete: n = 6
# sum of numbers from 1...6 should be 21
# (6 * 7) / 2

# desired_sum = 21

# actual sum = 26

# so there's an extra 5 somewhere
def appears_twice(lst):
    n = len(lst) - 1
    desired_sum = (n * (n + 1)) / 2
    print (desired_sum)
    actual_sum = sum(lst)
    print (actual_sum)
    print actual_sum - desired_sum

# 7 numbers, appear in the range 1-6
# n + 1 numbers in the range 1 - n
lst = [1, 2, 3, 4, 5, 5, 6]
appears_twice(lst)
