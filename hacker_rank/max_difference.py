# def max_difference(a):
#     max_difference = -float("inf")
#     for i in range(len(a)):
#         for j in range(i+1, len(a)):
#             if a[j] - a[i] > max_difference:
#                 max_difference = a[j] - a[i]
#     return max_difference

def max_difference(a):
    maxDifference = -float("inf")
    min_number = float("inf")

    for elem in a:
        if elem - min_number > maxDifference:
            maxDifference = elem - min_number
        if elem < min_number:
            min_number = elem

    return maxDifference

print "Max difference is", max_difference([2, 3, 10, 2, 4, 8, 1])
print "Max difference is", max_difference([7, 9, 5, 6, 3, 2])
