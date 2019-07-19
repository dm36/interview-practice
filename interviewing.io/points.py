import math
from collections import defaultdict

# Explanation for interviewing.io solution's runtime:
# https://en.wikipedia.org/wiki/Binary_heap
# https://wiki.python.org/moin/TimeComplexity
def eucledian_distance(point, vertex):
    x_dist = (point[0] - vertex[0]) ** 2
    y_dist = (point[1] - vertex[1]) ** 2

    dist = math.sqrt(x_dist + y_dist)
    return dist

def kth_closest(points, vertex, k):
    # Map distance to all the points having that distance
    # from the vertex
    dist_map = defaultdict(list)
    for point in points:
        print point
        distance = eucledian_distance(point, vertex)
        dist_map[distance].append(tuple(point))
    print dist_map

    kth_closest = []
    sorted_keys = sorted(dist_map.keys())
    count = 0

    # Take k values from the map- prioritizing by distance
    for dist in sorted_keys:
        lst = dist_map[dist]
        for i in range(len(lst)):
            count += 1
            kth_closest.append(lst[i])
            if count == k:
                return kth_closest


points = [[1, 2], [3, -1], [2, 1], [2, 3]]
vertex = [2, 2]
k = 2

print kth_closest(points, vertex, k)
