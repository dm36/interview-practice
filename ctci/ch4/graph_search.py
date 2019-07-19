import queue
import stack

def bfs(graph, start_node):
    parents = {start_node: None}
    dist = {start_node: 0}

    bfs_queue = queue.Queue()
    bfs_queue.add(start_node)

    # Pop a node from the queue- go through
    # all its unvisited neighbors and add those
    # to the parents mapping and the queue
    while bfs_queue.isEmpty() == False:
        node = bfs_queue.remove()
        for nbr in graph[node]:
            if nbr not in parents:
                parents[nbr] = node
                dist[nbr] = dist[node] + 1
                bfs_queue.add(nbr)

    return dist, parents

def bfs_route(graph, start_node, end_node):
    parents = {start_node: None}
    dist = {start_node: 0}

    if start_node == end_node:
        return True

    bfs_queue = queue.Queue()
    bfs_queue.add(start_node)

    # Pop a node from the queue- go through
    # all its unvisited neighbors and add those
    # to the parents mapping and the queue
    while bfs_queue.isEmpty() == False:
        node = bfs_queue.remove()
        if node == end_node:
            return True
        for nbr in graph[node]:
            if nbr not in parents:
                bfs_queue.add(nbr)

    return False

def dfs(graph, node):
    dist = {}
    parents = {node: None}

    for n in graph:
        dist[n] = float("inf")

    dist[node] = 0

    dfs_stack = stack.Stack()
    dfs_stack.push(node)

    while dfs_stack.isEmpty() == False:
        node = dfs_stack.pop()
        for nbr in graph[node]:
            # Marking distances and adding to the parents mapping
            # does not equate to exploring
            if dist[nbr] == float("inf"):
                parents[nbr] = node
                dist[nbr] = dist[node] + 1
                dfs_stack.push(nbr)

    return dist, parents

def recursive_dfs(graph, node, parents, dist):
    for nbr in graph[node]:
        if nbr not in parents:
            parents[nbr] = node
            dist[nbr] = dist[node] + 1
            recursive_dfs(graph, nbr, parents, dist)

def is_route(parents, start_node, end_node):
    node = end_node
    path = str(end_node) + "->"

    while node != start_node:
        node = parents[node]
        if node == start_node:
            path += str(node)
        else:
            path += str(node) + "->"

    print path
    return True

graph = {1: [2, 5], 2: [1, 3, 5], 3: [2, 4], 4: [3, 5, 6], 5: [1, 2, 4], 6: [4]}

dist1, parents1 = bfs(graph, 1)
print "BFS dist: ", dist1
print "BFS parents: ", parents1
print

dist2 = {1: 0}
parents2 = {1: None}
recursive_dfs(graph, 1, parents2, dist2)
print "Recursive DFS dist: ", dist2
print "Recursive DFS parents: ", parents2
print

dist3, parents3 = dfs(graph, 1)
print "DFS dist: ", dist3
print "DFS parents: ", parents3
print

print "Route between 1 and 6: "
print (bfs_route(graph, 1, 6))
print

print "Route between 1 and 6: "
print (is_route(parents1, 1, 6))
print
