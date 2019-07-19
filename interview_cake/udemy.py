# Could just use linear search and find the
# earliest word (updating earliest word if the
# current word is alphabetically before earliest word)
def find_rotation_point_linear(arr):
    min_word = "z"
    for word in arr:
        if word < min_word:
            min_word = word
    print min_word

# words = ['k', 'v', 'a', 'b', 'c', 'd', 'e', 'g', 'i']

# idea is comparing the first element in the array
# repeatedly against the element at the middle index- and using
# that to determine the search space

# i.e. c is < k which indicates that the rotation point is to
# the left- so we set the high index to mid - 1

# O(log n) time, O(1) space
def rotation_point(arr, low, high):
    while low < high:
        mid = (low + high) / 2

        # Why set high to mid and not mid - 1?
        # or low not to be mid + 1?
        if arr[mid] < arr[0]:
            high = mid
        else:
            low = mid

        # Why return high in this case?
        if low + 1 == high:
            return high


words = [
'ptolemaic',
'retrograde',
'supplant',
'undulate',
'xenoepist',
'asymptote',  # <-- rotates here!
'babka',
'banoffee',
'engender',
'karpatka',
'othellolagkage',
]

letters = ['k', 'v', 'a', 'b', 'c', 'd', 'e', 'g', 'i']

# find_rotation_point_linear(words)
print (rotation_point(words, 0, len(words) - 1))
print (rotation_point(letters, 0, len(letters) - 1))
