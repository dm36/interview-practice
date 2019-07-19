import copy

def rotate(arr):
    arr2 = copy.deepcopy(arr)

    temp = arr2[0][0]

    arr2[0][0] = arr[2][0]
    arr2[2][0] = arr[2][2]
    arr2[2][2] = arr[0][2]
    arr2[0][2] = temp

    for row in arr2:
        print row

arr = [ [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9] ]
rotate(arr)

# should look like
# [ [7, 4, 1],
#   [8, 5, 2]
#   [9, 6, 3] ]
