def two_sum(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] + arr[j] == target:
                return i, j

def two_sum_hash(arr, target):
    hash_map = {}
    for i in range(len(arr)):
        if target - arr[i] in hash_map:
            return hash_map[target - arr[i]], i
        else:
            hash_map[arr[i]] = i
    return -1

def two_sum_pointers(arr, target):
    i, j = 0, len(arr) - 1
    while i < j:
        if arr[i] + arr[j] == target:
            return i, j
        elif arr[i] + arr[j] < target:
            i += 1
        elif arr[i] + arr[j] > target:
            j -= 1
    return -1

def two_sum_binary_search(arr, target):
    for i in range(len(arr)):
        j = binary_search_helper(arr, target - arr[i], 0, len(arr) - 1)
        if j != -1:
            return i, j

def binary_search_helper(arr, target, lo, hi):
    if lo > hi:
        return -1

    mid = (lo + hi) / 2
    if target == arr[mid]:
        return mid
    # go left
    elif target < arr[mid]:
        return binary_search_helper(arr, target, lo, mid - 1)
    elif target > arr[mid]:
        return binary_search_helper(arr, target, mid + 1, hi)

def binary_search(arr, target):
    return binary_search_helper(arr, target, 0, len(arr) - 1)

def binary_search_iterative(arr, target):
    lo, hi = 0, len(arr) - 1

    while lo <= hi:
        mid = (lo + hi) / 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            hi = mid - 1
        elif target > arr[mid]:
            lo = mid + 1

    return -1

# print (two_sum([1, 2, 3, 4, 5, 6], 7))
# print (two_sum_hash([1, 2, 3, 4, 5, 6], 7))
# print (two_sum_pointers([1, 2, 3, 4, 5, 6], 7))
print (binary_search([1, 2, 3, 4, 5, 6, 8], 8))
print (two_sum_binary_search([1, 2, 3, 4, 5, 6, 8], 8))
