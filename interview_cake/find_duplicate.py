from collections import Counter

# sort and check adjacent elements to find
# an integer that appears more than once

# n*logn + n runtime or O(nlogn), O(1) space
def find_duplicate(lst):
    lst.sort()
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]:
            return lst[i]

def find_duplicate_counter(lst):
    num_count = Counter(lst)
    print num_count
     num_count.most_common(1)[0][1]

# O(n) runtime O(n) space, O(n) runtime because have
# to go through all the elements of a list, O(n) space
# because have to use a set
def find_duplicate_set(lst):
    numbers_seen = set()

    # add elements to a set and if an element
    # is already in the set- we have our duplicate!
    # for i in range(len(lst)-1):
    #     if lst[i] in numbers_seen:
    #         return lst[i]
    #     else:
    #         numbers_seen.add(lst[i])

    # really no need for indices
    for number in lst:
        if number in numbers_seen:
            return number
        else:
            numbers_seen.add(number)

print "Find duplicate Counter: "
print find_duplicate_counter([1, 2, 3, 4, 5, 6, 6])
print find_duplicate_counter([6, 6, 1, 2, 3, 4, 5])
print

print "Find duplicate sort: "
print find_duplicate([1, 2, 3, 4, 5, 6, 6])
print find_duplicate([6, 6, 1, 2, 3, 4, 5])
print

print "Find duplicate with sets: "
print find_duplicate_set([1, 2, 3, 4, 5, 6, 6])
print find_duplicate_set([6, 6, 1, 2, 3, 4, 5])

# Other thought is we could use the modified binary search to find
# the left-most and right-most occurrence of a number, and if these
# indices differ that's our duplicate- we'd have to run this on every
# number in the array

# Binary search is O(log(n))- number of times we break our list
# until we find the desired number, we'd have to do run binary search
# 2n times so O(n * log(n)), we'd also have to sort the array which is O(nlogn)
# so O(nlogn), O(1) space

# https://stackoverflow.com/questions/8185079/how-to-calculate-binary-search-complexity
