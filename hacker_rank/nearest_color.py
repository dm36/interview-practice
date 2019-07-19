#!/bin/python

import math
import os
import random
import re
import sys
import collections

# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#
class Queue:
    def __init__(self):
        self.q = []
    def add(self, x):
        self.q.append(x)
    def pop(self):
        return self.q.pop(0)
    def len(self):
        return len(self.q)

# general idea- bfs from start node- if the node has the same color
# as the start node store its distance from the start node

# return smallest observed distance
def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    graph = collections.defaultdict(list)

    for i in range(len(graph_from)):
        graph[graph_from[i]].append(graph_to[i])
        graph[graph_to[i]].append(graph_from[i])

    queue = Queue()
    queue.add(val)

    start_color = ids[val-1]

    dist = {}
    parents = {}
    color_dist = []

    for node in graph:
        dist[node] = float("inf")

    dist[val] = 0
    parents[val] = None

    while queue.len() > 0:
        node = queue.pop()
        for nbr in graph[node]:
            if nbr not in parents:
                dist[nbr] = dist[node] + 1
                parents[nbr] = parents[node]
                queue.add(nbr)

                nbr_color = ids[nbr-1]
                if start_color == nbr_color:
                    color_dist.append(dist[nbr])

    if len(color_dist):
        return min(color_dist)
    else:
        return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    graph_nodes, graph_edges = map(int, raw_input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in xrange(graph_edges):
        graph_from[i], graph_to[i] = map(int, raw_input().split())

    ids = map(long, raw_input().rstrip().split())

    val = int(raw_input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    fptr.write(str(ans) + '\n')

    fptr.close()
