# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
#
# The distance between two adjacent cells is 1.

# Input:
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]
#
# Output:
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]

# run dfs on each cell
# question is how will dfs work?
# basically as long as we're in the bounds of the matrix
# check the top square, left square, right square and bottom square
# if any are out of bounds return False or -1 or something as such
# for the base case
# pass dist as 0 as the argument
# if the value is 0 return 1 + dist?
# if not a 0- continue recursion

# Input:
# [[0,0,0],
#  [0,1,0],
#  [1,1,1]]
#
# Output:
# [[0,0,0],
#  [0,1,0],
#  [1,2,1]]

class Queue():
    def __init__(self, ):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        return self.queue.pop(0)
    def len(self):
        return len(self.queue)

# def helper_dfs(i, j, matrix, dist):
#     if (i > len(matrix) - 1 or i < 0) or (j > len(matrix[0]) - 1 or j < 0):
#         return -1
#     elif matrix[i][j] == 0:
#         return dist
#     else:
#         a = helper_dfs(i + 1, j, matrix, dist + 1)
#         b = helper_dfs(i - 1, j, matrix, dist + 1)
#         c = helper_dfs(i, j - 1, matrix, dist + 1)
#         d = helper_dfs(i, j + 1, matrix, dist + 1)
#         return min(a, b, c, d)

def helper_bfs(i, j, matrix, dist):
    queue = Queue()
    queue.enqueue((i, j, dist))
    while queue.len():
        x, y, distance = queue.dequeue()
        if (x > len(matrix) - 1 or x < 0) or (y > len(matrix[0]) - 1 or y < 0):
            continue
        if matrix[x][y] == 0:
            return distance

        queue.enqueue((x - 1, y, distance + 1))
        queue.enqueue((x + 1, y, distance + 1))
        queue.enqueue((x, y - 1, distance + 1))
        queue.enqueue((x, y + 1, distance + 1))


def updateMatrix(matrix):
    final_matrix = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[0])):
            row.append(0)
        final_matrix.append(row)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            final_matrix[i][j] = helper_bfs(i, j, matrix, 0)
    print (final_matrix)

my_matrix_2 = [[0,0,0],
 [0,1,0],
 [0,0,0]]

my_matrix = [[0,0,0],
 [0,1,0],
 [1,1,1]]
updateMatrix(my_matrix_2)
