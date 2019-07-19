# If 0 is not in the array return that-
#   - If the array was sorted we simply check the first element
#   - If the array was not sorted we'd have do an operation which
#     would cost us O(n)
#
# Sort the array and then iterate through the array- checking to see
# if the difference between elements is 1, the first place where
# this is not the case would be our smallest non-negative integer

# Specifically the first non-negative integer would be 1 + that previous
# number

# If we reach the end of the array return the last element + 1

# O(nlogn), O(1)

# Max element in the array- build a list of elements from 0 to that max element
# and take the difference

# [0, 1, 4, 6]

# [0, 1, 2, 3, 4, 5, 6]

# Greedily go through
def get_different_number(arr):
  arr.sort()
  if arr[0] != 0:
    return 0

  for i in range(1, len(arr)):
    diff = arr[i] - arr[i-1]
    if diff > 1:
      return arr[i-1] + 1

  return arr[-1] + 1

print get_different_number([0, 1, 2, 3])
print get_different_number([0, 1, 4, 6])
print get_different_number([6, 1, 4, 0])


# [0, 1, 2, 3, 4, 5]

# [0, 1, 4, 6]

# Length of the array is 4
# pigeon-hole principle
# pigeons: 0, 1, 2, 3, 4
# holes: [x, y, z, w]
# [6, 1, 4, 0]

# General principle: if the array's length is n, then the smallest non-negative integer has to be one of
# 0, 1, 2, 3, ..., n

def get_different_number(arr):
  s = set(arr)
  for i in range(n+1):
    if i not in s:
      return i
    s.add(i)

get_different_number([1, 2, 3, 6, 8])

# [1, 2, 3, 5, 8]
# [5, 1, 2, 3, 8]
# O(1)
#
# function getDifferentNumber(arr):
#     n = arr.length
#     temp = 0
#
#     # put each number in its corresponding index, kicking out
#     # the original number, until the target index is out of range.
#     for i from 0 to n-1:
#         temp = arr[i]
#         while (temp < n AND arr[temp] != temp):
#             swap(temp, arr[temp])
#
#     for i from 0 to n - 1:
#         if (arr[i] != i):
#             return i  # i isn’t in arr, hence we can return it
#
#     # we got here since every number from 0 to n-1 is in arr.
#     # By definition then, n isn’t in arr. Otherwise, the size of arr
#     # would have been n+1 and not n.
#     return n


# Repeatedly find the min and add 1- and check to see if that is in the array
