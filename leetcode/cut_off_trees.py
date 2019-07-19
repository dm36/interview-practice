# You are asked to cut off trees in a forest for a golf event.
# The forest is represented as a non-negative 2D map, in this map:
#
# 0 represents the obstacle can't be reached.
# 1 represents the ground can be walked through.
# The place with number bigger than 1 represents a tree can be walked through,
# and this positive number represents the tree's height.

# You are asked to cut off all the trees in this forest in the order of tree's height -
# always cut off the tree with lowest height first. And after cutting, the original place
# has the tree will become a grass (value 1).
#
# You will start from the point (0, 0) and you should output the minimum
# steps you need to walk to cut off all the trees. If you can't cut off all the trees,
# output -1 in that situation.
#
# You are guaranteed that no two trees have the same height and there is at least
# one tree needs to be cut off.
#
# Example 1:
#
# Input:
# [
#  [1,2,3],
#  [0,0,4],
#  [7,6,5]
# ]
# Output: 6
#
#
# Example 2:
#
# Input:
# [
#  [1,2,3],
#  [0,0,0],
#  [7,6,5]
# ]
# Output: -1
#
#
# Example 3:
#
# Input:
# [
#  [2,3,4],
#  [0,0,5],
#  [8,7,6]
# ]
# Output: 6
# Explanation: You started from the point (0,0) and you can cut off the tree in (0,0) directly without walking.

# bfs from point (0, 0) going both left, right, bottom, top
# if out of bounds return
# if value is not 1 greater than the previous tree also return (so need to pass the value along)
# visited set to mark that everything has been covered

visited = []

class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        return self.queue.pop(0)
    def len(self):
        return len(self.queue)

# def helper_dfs(forest, i, j, prev_tree, distance):
#     if (i < 0 or i > len(forest) - 1) or (j < 0 or j > len(forest[0]) - 1):
#         return -1
#     elif len(visited) == (len(forest) * len(forest[0])):
#         print distance, visited
#         return distance
#
#     visited.append((i, j))
#     helper_dfs(forest, i - 1, j, forest[i][j], distance + 1)
#     helper_dfs(forest, i + 1, j, forest[i][j], distance + 1)
#     helper_dfs(forest, i, j + 1, forest[i][j], distance + 1)
#     helper_dfs(forest, i, j - 1, forest[i][j], distance + 1)

def bfs(forest):
    queue = Queue()
    queue.enqueue((0, 0, forest[0][0], 0))
    visited = []
    distance = 0

    while queue.len():
        i, j, prev, distance = queue.dequeue()
        print (i, j, prev, distance)
        if (i < 0 or i > len(forest) - 1) or (j < 0 or j > len(forest[0]) - 1):
            continue
        if (i, j) != (0, 0) and forest[i][j] - prev < 1:
            continue
        visited.append((i, j))
        print visited
        if len(visited) == (len(forest) * len(forest[0])):
            print distance
            return distance

        if (i - 1, j) not in visited:
            queue.enqueue((i - 1, j, forest[i][j], distance + 1))
        if (i + 1, j) not in visited:
            queue.enqueue((i + 1, j, forest[i][j], distance + 1))
        if (i, j - 1) not in visited:
            queue.enqueue((i, j - 1, forest[i][j], distance + 1))
        if (i, j + 1) not in visited:
            queue.enqueue((i, j + 1, forest[i][j], distance + 1))

def cutOffTree(forest):
    return bfs(forest)
    # return helper_dfs(forest, 0, 0, forest[0][0], 0)

print (cutOffTree([[1,2,3],[0,0,4],[7,6,5]]))
