import math
import heapq

# Relevant links:
# https://en.wikipedia.org/wiki/Binary_heap
# https://docs.python.org/2/library/heapq.html
# https://github.com/python/cpython/blob/2.7/Lib/heapq.py

def eucledian_distance(point, vertex):
    x_dist = (point[0] - vertex[0]) ** 2
    y_dist = (point[1] - vertex[1]) ** 2

    dist = math.sqrt(x_dist + y_dist)
    return dist

# Pseudocode:

# 1) Compute each point's distance from the vertex
# 2) Push tuple of distance and point onto min heap
# 3) Pop k of these tuples, return the points
def kth_closest(points, vertex, k):
    h = []
    for point in points:
        dist = eucledian_distance(point, vertex)
        heapq.heappush(h, (dist, point))

    final = []
    for i in range(k):
        dist, point = heapq.heappop(h)
        final.append(point)
    return final

# Pseudocode:

# K-sized heap containing points w/ the smallest distance from
# the vertex

# 1) Compute each point's distance from the vertex
# 2) Flip it so it's -, we're maintaining a max heap
# 3) If the length of the heap is less than k, push tuple
#    of distance and the point onto the heap
# 4) If the length of the heap is equal to k, get the point with the largest
#    distance from the vertex (that is stored in the heap),
#    check if the distance for the point in consideration (from the vertex obvi)
#    is less than this point, and if so go ahead and replace it
#
#  Implementation specifics for step 4 (this is a bit confusing bc of the - approach)-
#  1) Use nsmallest with 1 to get the point in the heap with the largest distance
#     from the vertex
#  2) If the point's distance is greater than the largest distance (i.e. in actuality
#     smaller) do a pushpop with that point and its distance
#
# Ex:
# -1 (dist)
# -3.16 (largest_dist)

def kth_closest_opt(points, vertex, k):
    h = []
    for point in points:
        dist = eucledian_distance(point, vertex)
        dist = -dist
        if len(h) < k:
            heapq.heappush(h, (dist, point))
        elif len(h) == k:
            largest_dist, largest_point = heapq.nsmallest(1, h)[0]
            if dist > largest_dist:
                heapq.heappushpop(h, (dist, point))

    final = []
    for i in range(k):
        dist, point = heapq.heappop(h)
        final.append(point)
    return final

points = [[1, 2], [3, -1], [2, 1], [2, 3]]
vertex = [2, 2]
k = 2

print kth_closest(points, vertex, k)
print kth_closest_opt(points, vertex, k)
