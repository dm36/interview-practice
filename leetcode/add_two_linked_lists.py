class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def insert(self, val):
        if not self.head:
            self.head = Node(val)
            return

        tmp = self.head

        while tmp.next:
            tmp = tmp.next

        tmp.next = Node(val)

    def reverse(self):
        tmp = self.head
        prev = None

        while tmp:
            next = tmp.next
            tmp.next = prev
            prev = tmp
            tmp = next

        self.head = prev
        return prev

    def str(self):
        tmp = self.head

        while tmp:
            print tmp.val
            tmp = tmp.next

class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

# 1
# 2 4 3
# 5 6 4
# 8 0 7

# so can't start at the end and work toward the front

# first need to reverse both linked lists

# 2 4 3
# 5 6 4

#   1
# 3 4 2
# 4 6 5

# 7 0 8

# and then add from the beginning to the end
# handling carry over
# and then reverse the result

# form two integers

def addTwoNumbers(l1, l2):
    while l1:

    # l1.reverse()
    # l2.reverse()
    # l1.str()
    # l2.str()


# https://leetcode.com/problems/add-two-numbers/solution/




ll = LinkedList()
ll.insert(2)
ll.insert(4)
ll.insert(3)

# print ll.head.val
# print ll.head.next.val
# print ll.head.next.next.val
# print

# ll.reverse()

# print ll.head.val
# print ll.head.next.val
# print ll.head.next.next.val
# print

ll2 = LinkedList()
ll2.insert(5)
ll2.insert(6)
ll2.insert(7)

addTwoNumbers(ll.head, ll2.head)

# print ll2.head.val
# print ll2.head.next.val
# print ll2.head.next.next.val
# print

# ll2.reverse()
#
# print ll2.head.val
# print ll2.head.next.val
# print ll2.head.next.next.val
