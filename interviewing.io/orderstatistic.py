import pdb

def min_me(arr):
    min = float("inf")
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
    return min

# def second_order_statistic(arr):
#     min_element = min_me(arr)
#     min = arr[0]
#     for i in range(1, len(arr)):
#         if arr[i] > min_element and arr[i] < min:
#             min = arr[i]
#     return min

# If add a parameter n and want to find the nth smallest- and you extend
# this idea of storing n min's what would the runtime be? The runtime would
# be n^2 because you would be checking against all n during each iteration
# of the list
def second_order_statistic(arr):
    min = float("inf")
    min2 = float("inf")

    for i in range(len(arr)):
        if arr[i] < min:
            min2 = min
            min = arr[i]
        elif arr[i] < min2:
            min2 = arr[i]

    return min2

def nth_order_statistic(arr, n):
    arr.sort()
    return arr[n-1]

# https://www.geeksforgeeks.org/quick-sort/
def partition(array, start, end):
    pivot = array[end] # set pivot to the last element in the arr
    pindex = start # set pindex to the start of the arr

    for i in range(start, end):
        if array[i] <= pivot:
            temp = array[i]
            array[i] = array[pindex]
            array[pindex] = temp
            pindex += 1

    temp = array[pindex]
    array[pindex] = array[end]
    array[end] = array[pindex]
    print array

# print second_order_statistic([-199, 10, 3, 4, 5, 6])
# print second_order_statistic([0, 2, 3, 6])
# print nth_order_statistic([2, 3, 6, 0], 3)

arr = [2, 1, 3, 6, 8, 5, 7]
print partition(arr, 0, len(arr) - 1)
print arr
