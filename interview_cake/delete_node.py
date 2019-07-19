class LinkedList():
    def __init__(self, head):
        self.head = head

    def add(self, node):
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = node

    def delete_node(self, node):
        temp = self.head
        while temp.next != None:
            if temp.next.value == node.value:
                temp.next = temp.next.next
                return
        return "This node does not exist in the linked list"
        
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

def delete_node(node):
    # copy over the next node's value and next
    # pointer to the current node
    if node.next:
        node.value = node.next.value
        node.next = node.next.next


ll = LinkedList(Node('A'))
ll.add(Node('B'))
ll.add(Node('C'))

print ll.head.value
print ll.head.next.value
print ll.head.next.next.value

ll.delete_node(Node('B'))

print
print ll.head.value
print ll.head.next.value
