class LinkedList():
    def __init__(self, head):
        self.head = head

    def insert(self, node):
        temp = self.head

        while temp.next != None:
            temp = temp.next

        temp.next = node

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

# def contains_cycle(head):
#     walker = head
#     runner = head.next
#
#     # For test case 1:
#     # Before while loop: walker is set to Node a, runner is set to Node b
#     # Iteration 1: walker- Node b, runner Node d
#     # Iteration 2: walker- Node c, runner Node b
#     # Iteration 3: walker- Node d, runner Node d
#     # we break out and return True
#
#     # For test case 2:
#     # Before while loop- walker is set to Node a, runner is set to Node b
#     # Iteration 1: walker- Node b, runner, Node d
#     # Runner has no next- so we break out and return False
#
#     # If we didn't have a cycle- we would break out of the while loop
#     # when runner didn't have a next- and then return False
#     while runner.next:
#         print walker.value, runner.value
#         if walker == runner:
#             return True
#         walker = walker.next
#         runner = runner.next.next
#
#     return False

# O(n) time and O(1) space.
#
# The runtime analysis is a little tricky.
# The worst case is when we do have a cycle,
# so we don't return until fast_runner equals slow_runner.
# But how long will that take?
#
# First, we notice that when both runners are circling
# around the cycle fast_runner can never skip over slow_runner.
# Why is this true?
#
# Suppose fast_runner had just skipped over slow_runner.
# fast_runner would only be 1 node ahead of slow_runner,
# since their speeds differ by only 1.
# So we would have something like this:
#
#   [ ] -> [s] -> [f]
# What would the step right before this "skipping step" look like?
# fast_runner would be 2 nodes back, and slow_runner would be 1 node back.
# But wait, that means they would be at the same node!
# So fast_runner didn't skip over slow_runner! (This is a proof by contradiction.)
#
# Since fast_runner can't skip over slow_runner,
# at most slow_runner will run around the cycle once
# and fast_runner will run around twice.
# This gives us a runtime of O(n).
# def contains_cycle(head):
#     walker = head
#     runner = head
#
#     # For test case 1:
#     # Before while loop: walker is set to Node a, runner is set to Node a
#     # Iteration 1: walker- Node b, runner Node c
#     # Iteration 2: walker- Node c, runner Node b
#     # Iteration 3: walker- Node d, runner Node d
#     # we break out and return True
#
#     # For test case 2:
#     # Before while loop- walker is set to Node a, runner is set to Node a
#     # Iteration 1: walker- Node b, runner Node c
#     # Iteration 2: walker- Node c, runner Node a
#     # Iteration 3: walker- Node d, runner Node None
#     # So none.next causes an error- which is why we also need to
#     # check while runner
#
#     # If we didn't have a cycle- we would break out of the while loop
#     # when runner didn't have a next- and then return False
#     while runner and runner.next:
#         walker = walker.next
#         runner = runner.next.next
#
#         if walker == runner:
#             return True
#
#     return False

# O(n) runtime, O(n) space
def contains_cycle(head):
    node = head
    nodes = set([])

    # Add each node to the linked list
    # If a node has been added to the set before return True
    # Otherwise- set node to node.next
    while node:
        if node in nodes:
            return True
        nodes.add(node)
        node = node.next

    return False

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

ll = LinkedList(a)
ll.insert(b)
ll.insert(c)
ll.insert(d)
ll.insert(a)
print contains_cycle(a)

a1 = Node("a")
b1 = Node("b")
c1 = Node("c")
d1 = Node("d")

ll = LinkedList(a1)
ll.insert(b1)
ll.insert(c1)
ll.insert(d1)
print contains_cycle(a1)
