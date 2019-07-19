def get_different_number(arr):
  s = set(arr)
  n = len(arr)

  # going through all numbers between 0 and the length of the array
  # and finding the first one that is not in the array
  for i in range(n+1):
    # set is implemented as a hash table so membership is O(1)
    if i not in s:
      return i
    s.add(i)

print get_different_number([0, 1, 2, 4])
