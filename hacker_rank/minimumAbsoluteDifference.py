# def minimumAbsoluteDifference(arr):
#     min_diff = float("inf")
#
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if i != j:
#                 abs_diff = abs(arr[i] - arr[j])
#                 if abs_diff < min_diff:
#                     min_diff = abs_diff
#
#     return min_diff

# sort array and take absolute differences of adjacent
# elements
def minimumAbsoluteDifference(arr):
    arr.sort()
    min_diff = float("inf")
    for i in range(len(arr)-1):
        if (arr[i+1] - arr[i]) < min_diff:
            min_diff = arr[i+1] - arr[i]
    return min_diff



print (minimumAbsoluteDifference([-59,-36,-13,1,-53,-92,-2,-96,-54, 75]))
