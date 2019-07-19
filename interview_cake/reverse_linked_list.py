class LinkedList():
    def __init__(self, head):
        self.head = head

    def insert(self, node):
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node

    def reverse(self):
        temp = self.head
        prev = None

        while temp:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next

        self.head = prev
        return prev

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse(head):
    temp = head
    prev = None

    while temp:
        next = temp.next
        temp.next = prev
        prev = temp
        temp = next

    return prev

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

ll = LinkedList(a)
ll.insert(b)
ll.insert(c)
ll.insert(d)

new_head = reverse(a)
print new_head.value
print new_head.next.value
print new_head.next.next.value
print new_head.next.next.next.value

# ll.reverse()
# print ll.head.value
# print ll.head.next.value
# print ll.head.next.next.value
# print ll.head.next.next.next.value
