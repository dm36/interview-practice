import collections

# could also use collections.deque and popleft

# shortest route from a message from one user (sender) to another (receiver),
# return a list of users that make up this route

class Queue():
    def __init__(self):
        self.queue = []
    def add(self, elem):
        self.queue.append(elem)
    # want to return the first guy in the queue
    def pop(self):
        return self.queue.pop(0)
    def len(self):
        return len(self.queue)

# my_queue = Queue()
# my_queue.add(6)
# my_queue.add(5)
# my_queue.add(3)

# Run BFS- build a parents mapping and then
# use this mapping to build a route between a sender
# and a receiver
def bfs(network, sender, receiver):
    dist = collections.defaultdict(int)
    parents = collections.defaultdict(str)
    bfs_queue = Queue()
    arrived_at_receiver = False

    # Set parents for all users in the network to None
    for user in network:
        parents[user] = None

    # Add sender to the bfs queue
    bfs_queue.add(sender)

    # Keep this while loop going as long as there are nodes
    # to explore or we've arrived at the receiver
    while bfs_queue.len() > 0:
        user = bfs_queue.pop()

        # Go through all neighbors of a user
        # and if they've not been explored yet
        # set their parents- and then
        # add them to the queue so we can explore their
        # neighbors
        for nbr in network[user]:
            if parents[nbr] == None:
                parents[nbr] = user
                bfs_queue.add(nbr)

                # Once we've arrived at and filled out information about
                # the receiver we can break
                if nbr == receiver:
                    arrived_at_receiver = True

    if not arrived_at_receiver:
        return "No way for messages to get to recipient"

    # Build path from receiver -> sender
    # using parents mapping and then reverse it
    path = []
    user = receiver
    path.append(user)
    while user != sender:
        user = parents[user]
        path.append(user)

    path.reverse()
    print path

network = {
    'Min'     : ['William', 'Jayden', 'Omar'],
    'William' : ['Min', 'Noam'],
    'Jayden'  : ['Min', 'Amelia', 'Ren', 'Noam'],
    'Ren'     : ['Jayden', 'Omar'],
    'Amelia'  : ['Jayden', 'Adam', 'Miguel'],
    'Adam'    : ['Amelia', 'Miguel', 'Sofia', 'Lucas'],
    'Miguel'  : ['Amelia', 'Adam', 'Liam', 'Nathan'],
    'Noam'    : ['Nathan', 'Jayden', 'William'],
    'Omar'    : ['Ren', 'Min', 'Scott']
}

bfs(network, "Jayden", "Adam")
