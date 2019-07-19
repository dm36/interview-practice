import copy

def zeroMatrix(x):
    x2 = copy.deepcopy(x)

    # len(x2) is number of rows, len(x2[i]) is number of columns
    for i in range(len(x2)):
        for j in range(len(x2[i])):
            if x2[i][j] == 0:
                # Sets row to 0
                x[i] = [0] * len(x2[i])

                # Sets column to 0
                # len(x2) is the number of rows- so we're iterating over
                # all the rows and setting those at a given column to 0
                for i in range(len(x2)):
                    x[i][j] = 0

    return x

# Set flags to indicate whether there is a zero in a given
# row or a given column and use that info to set rows and cols to 0
def zeroMatrixEfficient(x):
    zero_this_row = [False] * len(x)
    zero_this_col = [False] * len(x[0])

    # i corresponds to row, j corresponds to column
    for i in range(len(x)):
        for j in range(len(x[i])):
            if x[i][j] == 0:
                zero_this_row[i] = True
                zero_this_col[j] = True


    print zero_this_row
    print zero_this_col

    # i is used as an index for rows, j is used
    # as an index for cols

    # (row, col1)... (row, # of cols) => 0
    for i in range(len(zero_this_row)):
        if zero_this_row[i] == True:
            for j in range(len(x[i])):
                x[i][j] = 0

    # (row1, col)... (row #, col) => 0
    for j in range(len(zero_this_col)):
        if zero_this_col[j] == True:
            for i in range(len(x)):
                x[i][j] = 0

    return x


print zeroMatrix([[5, 4, 3],
            [3, 2, 0],
            [1, 0, 5]])

print zeroMatrixEfficient(
            [[5, 4, 3],
            [3, 2, 0],
            [1, 0, 5]])
