def find_whitespace(arr, first_ind):
  for i in range(first_ind, len(arr)):
    if arr[i].isspace():
      return i
  return len(arr) - 1

def reverse_words(arr):
  # initial swap
  first_ind = 0
  final_ind = len(arr) - 1

  while first_ind < final_ind:
    arr[first_ind], arr[final_ind] = arr[final_ind], arr[first_ind]
    first_ind += 1
    final_ind -= 1


  whitespace_ind = 0
  first_ind = 0

  while whitespace_ind != len(arr) - 1:
    # swap from index to whitespace
    print first_ind, whitespace_ind

    # finds whitespace, saves next index to move to and
    # swaps
    whitespace_ind = find_whitespace(arr, first_ind) - 1
    next_ind = whitespace_ind + 1
    print first_ind, whitespace_ind, next_ind
    print arr

    while first_ind < whitespace_ind:
      arr[first_ind], arr[whitespace_ind] = arr[whitespace_ind], arr[first_ind]
      first_ind += 1
      whitespace_ind -= 1

    print first_ind, next_ind
    first_ind = next_ind + 1




arr = ['e', 'c', 'i', 't', 'c', 'a', 'r', 'p', ' ']
ind = 0
print arr.index(' ')

# have one index point at the first character
# and another at the last characeter- swap those elements
# and increment your first index and decrement your last index
# until the indices overlap

# issue with this is the word would reverse- so you'd have
# to go through each word and then reverse that using a similar
# process




# ['d', 'c', 'b', 'a']
#
#       |    |


arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ', 'm', 'a', 'k', 'e', 's', '  ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]
print reverse_words(arr)
