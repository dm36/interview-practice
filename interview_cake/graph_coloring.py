# Queue is FIFO- so we
# add to the end and pop from the front

class Queue:
    def __init__(self):
        self.queue = []
    def add(self, item):
        self.queue.append(item)
    def pop(self):
        return self.queue.pop(0)
    def len(self):
        return len(self.queue)
    def str(self):
        return str(self.queue)

def graph_coloring(graph):
    colors = ["red", "blue", "green", "orange", "black", "yellow", "purple"]
    queue = Queue()

    # pick start node to be the first node in the graph's keys and
    # the max degree to be the longest from all the lists of values
    start_node = graph.keys()[0]
    max_degree = max([len(nbrs) for nbrs in graph.values()])

    # limit colors to be of length d + 1
    colors = colors[:max_degree+1]
    color = {}

    # add start node to the queue
    queue.add(start_node)

    # First give every node a color of None
    for node in graph:
        color[node] = None

    # Give the start node the color red
    color[start_node] = colors[0]

    assigned_nbrs_color = []
    while queue.len() > 0:
        node = queue.pop()
        print "Node is:", node
        if node in assigned_nbrs_color:
            continue

        # Explore all the neighbors of the node
        for nbr in graph[node]:
            if nbr in assigned_nbrs_color:
                continue
            print "Neighbor is:", nbr
            # Assign each neighbor of the node a color
            # that is not shared with any of its neighbors
            colors_taken = [color[node]]
            for nbr_of_nbr in graph[nbr]:
                if nbr_of_nbr == node:
                    continue
                if color[nbr_of_nbr] != None:
                    colors_taken.append(color[nbr_of_nbr])
            print "Colors are :", colors
            print "Colors taken are  :", colors_taken
            possible_colors = list(set(colors).symmetric_difference(set(colors_taken)))
            print "Possible colors are :", possible_colors
            if len(possible_colors) == 0:
                return False
            color[nbr] = possible_colors[0]
            print color
            assigned_nbrs_color.append(node)
            queue.add(nbr)

def graph_coloring_simpler(graph):
    # building a colors array that is at most length max degree + 1
    colors = ["red", "blue", "green", "orange", "black", "yellow", "purple"]
    max_degree = max([len(nbrs) for nbrs in graph.values()])
    colors = colors[:max_degree+1]

    colors_dict = {}
    # initialize colors dict for each node
    for node in graph:
        colors_dict[node] = None

    # for each node in the graph- build a concept of colors that
    # are illegal to assign that node by using colors dict
    # with its neighbors.
    # assign the node a color that is not illegal
    for node in graph:
        legal_colors = []
        illegal_colors = []
        for nbr in graph[node]:
            if colors_dict[nbr] != None:
                illegal_colors.append(colors_dict[nbr])

        legal_colors = list(set(colors) - set(illegal_colors))
        colors_dict[node] = legal_colors[0]
        print colors_dict

        # list comprehensions read left to right other than the first thing
        # illegal_colors = [colors_dict[nbr] for nbr in graph[node] if colors_dict[nbr] != None]

graph = {1: [2, 5], 2: [1, 3, 5], 3: [2, 4], 4: [3, 5, 6], 5: [1, 2, 4], 6: [4]}

graph_coloring(graph)

# Given an undirected graph with max degree D-
# find a graph coloring using at most D+1 colors

# BFS- find the max degree (if the graph is represented
# as a dictionary from a node to all its neighbors, its
# max degree would be the max value length among all keys)
#
# network = {
#     'Min'     : ['William', 'Jayden', 'Omar'],
#     'William' : ['Min', 'Noam'],
#     'Jayden'  : ['Min', 'Amelia', 'Ren', 'Noam'],
#     'Ren'     : ['Jayden', 'Omar'],
#     'Amelia'  : ['Jayden', 'Adam', 'Miguel'],
#     'Adam'    : ['Amelia', 'Miguel', 'Sofia', 'Lucas'],
#     'Miguel'  : ['Amelia', 'Adam', 'Liam', 'Nathan'],
#     'Noam'    : ['Nathan', 'Jayden', 'William'],
#     'Omar'    : ['Ren', 'Min', 'Scott']
# }
#
# i.e. a graph represented as above would have a max degree of 4-
# we then build an array of d+1 (4+1) colors and assign a color
# to each node in the graph
#
# how do we assign colors to each node?

# Every-time we pick a node off the queue- we identify its color
# and assign all its neighbors colors that are not the color of that node- but
# that wouldn't necessarily work because we won't be keeping track of the colors
# of each of its neighbors' neighbors (and we might thereby assign two neighbors
# the same color)
# so everytime we explore a node's neighbors- we should look at all its neighbors neighbors
# unassigned or assigned and make sure we assign it an apt color
#
# best way to do this is keep a dictionary that maps nodes to their color
# and gives them a color of None if no such color exists
