class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

def delete_node(node):
    # If the node has a next set its value to the
    # next node and it's next to the next's node's next
    if node.next:
        node.value = node.next.value
        node.next = node.next.next

a = Node('A')
b = Node('B')
c = Node('C')

a.next = b
b.next = c

print a.value
print b.value
print c.value

print

print a.next.value
print b.next.value

print
delete_node(b)
print a.next.value
