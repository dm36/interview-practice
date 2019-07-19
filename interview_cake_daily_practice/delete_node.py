# LinkedList class- define with the head of the linked list
class LinkedList():
    def __init__(self, head):
        self.head = head

    # find the last node in the linked list
    # and insert the node after that node
    def insert(self, node):
        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = node

# Node has a concept of a value and a pointer
# to its next node
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

# To delete a node replace the contents of the current node
# with the next node's contents
def delete_node(node):
    if node.next:
        node.value = node.next.value
        node.next = node.next.next

node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

ll = LinkedList(node0)
ll.insert(node1)
ll.insert(node2)
ll.insert(node3)
ll.insert(node4)
ll.insert(node5)

print ll.head.value
print ll.head.next.value
print ll.head.next.next.value

delete_node(node2)

print
print ll.head.value
print ll.head.next.value
print ll.head.next.next.value
