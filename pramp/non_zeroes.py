# Store another array and copy over non-zero elements to that
# array, zero element increment a counter- append that many
# zeroes to the end of the array

# O(n) space
# O(n) runtime

# [1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]
# [1, 10, 2, 8, 3, 6, ]

# index of last non_zero element =
# count = 3

# O(n) time, O(1) space

def moveZerosToEnd(arr):
  non_zero_ind = 0

  for i in range(len(arr)):
    if arr[i] != 0:
      arr[non_zero_ind] = arr[i]
      non_zero_ind += 1

  for i in range(non_zero_ind, len(arr)):
    arr[i] = 0

  return arr


print moveZerosToEnd([1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0])
