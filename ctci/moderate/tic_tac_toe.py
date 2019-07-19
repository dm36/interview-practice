# # https://stackoverflow.com/questions/3844801/check-if-all-elements-in-a-list-are-identical

# Go through each row in the board and check to see if
# the # of instances of the first element is the same as the length
# of the row- this indicates we have all x's or all o's in a given row
def check_rows(board):
    for row in board:
        if row.count(row[0]) == len(row):
            return True
    return False

# Build an array of each column in the board
# and apply the same logic as used for check_rows
# (cols.count(cols[0]) == len(cols))
def check_cols(board):
    for i in range(len(board)):
        cols = []
        for j in range(len(board)):
            cols.append(board[j][i])
        if cols.count(cols[0]) == len(cols):
            return True
    return False

# Check both diagonals by comparing the first element in the diagonal
# against all other elements in the diagonal
def check_diagonals(board):
    flag = True
    for i in range(len(board)):
        if board[i][i] != board[0][0]:
            flag = False
            break
    if flag == True:
        return flag

    for i in range(len(board)):
        if board[i][len(board)-1-i] != board[0][len(board)-1]:
            return False
    return True

def did_win(board):
    return check_rows(board) or check_diagonals(board) or check_cols(board)

print did_win([['o', 'x', 'x'],
               ['o', 'o', 'x'],
               ['x', 'o', 'x']])
