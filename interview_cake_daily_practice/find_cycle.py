class LinkedList():
    def __init__(self, head):
        self.head = head

    def insert(self, node):
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

# Example 1:
# walker a, runner b

# While loop:
# walker- b, runner- d
# break out and return False

# Example 2:
# Walker a, runner b

# While loop
# walker- b, runner b

# Iteration 1 of while loop:
# walker gets set to b, runner to c
def contains_cycle(node):
    walker = node
    runner = node.next
    print walker.value, runner.value

    while runner.next:
        print walker.value, runner.value
        if walker == runner:
            return True
        walker = node.next
        runner = runner.next.next

    return False

# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
#
# ll = LinkedList(a)
# ll.insert(b)
# ll.insert(c)
# ll.insert(d)
#
# print ll.head.value
# print ll.head.next.value
# print ll.head.next.next.value
# print ll.head.next.next.next.value

# print contains_cycle(a)

a1 = Node('a')
b1 = Node('b')

ll2 = LinkedList(a1)
ll2.insert(b1)
ll2.insert(a1)

print contains_cycle(a1)
