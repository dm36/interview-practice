from collections import Counter

def binary_search(arr, elem, low, high):
    if low > high:
        return -1
    mid = (low + high) / 2
    if arr[mid] == elem:
        return mid
    # remember the + 1 and -1 in the indices!! otherwise
    # infinite recursion :(
    elif arr[mid] < elem:
        return binary_search(arr, elem, mid + 1, high)
    elif arr[mid] > elem:
        return binary_search(arr, elem, low, mid - 1)

arr = [2, 4, 10, 10, 10, 18, 20]

print "Testing recursive binary search: "
print binary_search(arr, 2, 0, len(arr) - 1)
print binary_search(arr, 4, 0, len(arr) - 1)
print binary_search(arr, 10, 0, len(arr) - 1)
print binary_search(arr, 18, 0, len(arr) - 1)
print binary_search(arr, 20, 0, len(arr) - 1)
print

def binary_search_iterative(arr, elem, low, high):
    while low <= high:
        mid = (low + high) / 2
        if arr[mid] == elem:
            return mid
        elif arr[mid] < elem:
            low = mid + 1
        elif arr[mid] > elem:
            high = mid - 1

print "Testing iterative binary search: "
print binary_search_iterative(arr, 2, 0, len(arr) - 1)
print binary_search_iterative(arr, 4, 0, len(arr) - 1)
print binary_search_iterative(arr, 10, 0, len(arr) - 1)
print binary_search_iterative(arr, 18, 0, len(arr) - 1)
print binary_search_iterative(arr, 20, 0, len(arr) - 1)
print

def binary_search_iterative_first(arr, elem, low, high):
    res = -1
    # if we find the element at mid
    # we store away mid as a potential index of the first instance
    # and then confine our search space to (low, mid - 1)
    while low <= high:
        mid = (low + high) / 2
        if arr[mid] == elem:
            res = mid
            high = mid - 1
        elif arr[mid] < elem:
            low = mid + 1
        elif arr[mid] > elem:
            high = mid - 1
    return res

print "First location of 10: "
print binary_search_iterative_first(arr, 10, 0, len(arr) - 1)
print

def binary_search_iterative_last(arr, elem, low, high):
    res = -1

    # So now that we're searching for the last instance of an element
    # not just any time the element occurs- so if we find the element at mid
    # we store away mid as a potential index of the last instance
    # and then confine our search space to (mid + 1, high)
    while low <= high:
        mid = (low + high) / 2
        if arr[mid] == elem:
            res = mid
            low = mid + 1
        elif arr[mid] < elem:
            low = mid + 1
        elif arr[mid] > elem:
            high = mid - 1
    return res

print "Last location of 10: "
print binary_search_iterative_last(arr, 10, 0, len(arr) - 1)
print

def count_occurrences(arr, elem):
    first = binary_search_iterative_first(arr, elem, 0, len(arr) - 1)
    last = binary_search_iterative_last(arr, elem, 0, len(arr) - 1)
    return last - first + 1

def count_occurrences_counter(arr, elem):
    return Counter(arr)[elem]

print "Count occurences:"
print (count_occurrences([2, 4, 10, 10, 10, 10, 10], 10))
print (count_occurrences_counter([2, 4, 10, 10, 10, 10, 10], 10))
