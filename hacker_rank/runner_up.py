def runner_up(arr):
    arr.sort()
    max = arr[-1]

    for i in range(len(arr)-1, -1, -1):
        if arr[i] != max:
            return arr[i]

print runner_up([2, 3, 6, 6, 5])

# first_max = float("-inf")
# second_max = float("-inf")
#
# for elem in arr:
#     if elem > first_max:
#         second_max = first_max
#         first_max = elemf
#     elif elem > second_max:
#         second_max = elem
#
# print second_max
