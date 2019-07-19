# what about two sum if the array is sorted in ascending order?
# use binary search!

# array is sorted
# so if the element you're looking for is greater than the
# element at arr[(low + high)/2] recurse to the right, i.e.
# setting your low to mid
# if the element you're looking for is less than the element
# at arr[(low + high)/2] recurse to the left, i.e. set
# the high to mid
def binary_search(arr, elem, lo, hi):
    if lo >= hi:
        return -1
    mid = (lo + hi)/2
    if arr[mid] == elem:
        return mid
    elif arr[mid] < elem:
        return binary_search(arr, elem, mid + 1, hi)
    else:
        return binary_search(arr, elem, lo, mid - 1)

# iterate through every element in the array and
def two_sum(arr, target):
    for i in range(len(arr)):
        elem = arr[i]
        other = binary_search(arr, target - elem, i+1, len(arr))
        if other != -1:
            print i, other

arr = [1, 2, 3, 4, 5, 6]
binary_search(arr, 7, 0, len(arr)-1)

two_sum([1, 2, 3, 4, 5, 6], 8)
two_sum([1, 2, 3, 4, 5, 6], 7)
two_sum([1, 2, 3, 4, 5, 6], 6)
