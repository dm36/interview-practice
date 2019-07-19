
def diagonal_difference(arr):
    first_diag = 0
    for i in range(len(arr)):
        first_diag += arr[i][i]
    print first_diag

    second_diag = 0
    for i in range(len(arr)):
        second_diag += arr[i][len(arr) - i - 1]
    return abs(first_diag - second_diag)

arr = [[1, 2, 3],
       [4, 5, 6],
       [9, 8, 9]]

print diagonal_difference(arr)
