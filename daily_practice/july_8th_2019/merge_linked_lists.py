# Reverse a link list

# 1 -> 2 -> 3
# 3 -> 2 -> 1

# retrieve the head

# set previous to be None

# save away the next node in the linked list
# set the next node to the previous
# update the previous
# update current to be current.next

class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def insert(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            return

        temp = self.tail
        temp.next = node
        self.tail = node

#         temp = self.head

#         while temp.next:
#             temp = temp.next

#         temp.next = node

    def prepend(self, node):
        temp = self.head
        self.head = node
        self.head.next = temp

    def reverse(self):
        temp = self.head  # 1
        prev = None
        self.tail = temp

        while temp:
            saved_next = temp.next # 2
            temp.next = prev # 1 <- -> 2 3
            prev = temp # prev becomes 1
            temp = saved_next #

        self.head = prev

    def print_linked_list(self):
        temp = self.head

        while temp:
            print temp.value
            temp = temp.next

    def len(self):
        temp = self.head
        count = 0

        while temp:
            count += 1
            temp = temp.next

        return count

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# 99 99
# assume longer linked list comes first

# 99 9

# l1 = 9->9
# l2 = 9

# carry_over = 0

# temp1 = 9
# temp2 = 9

# 18
# carry over = 1
# insert 8

# l3 = 8

# temp1 = 9
# temp2 = None

# l3 = 9 + 1


# time complexity
# reverse: O(n) + O(m)


# 99 9

# 99 09

# reversed:
# 99
# 90

# 189

# 123
# 456

def add_two_linked_lists(l1, l2):
    # prepend 0's to the second linked list
    diff = l1.len() - l2.len()
    while diff:
        l2.prepend(Node(0))
        diff -= 1

    # reverse the two linked lists
    l1.reverse()
    l2.reverse()

    # define a third linked list and set carry
    # over to 0
    l3 = LinkedList()
    carry_over = 0

    temp1 = l1.head
    temp2 = l2.head

    # as long as temp1 and temp2 are not None
    # keep iterating
    while temp1 and temp2:
        my_sum = temp1.value + temp2.value + carry_over
        carry_over = (my_sum / 10)
        l3.insert(Node(my_sum % 10))

        temp1 = temp1.next
        temp2 = temp2.next

    # insert the carry over at the end
    if carry_over > 0:
        l3.insert(Node(carry_over))

    # reverse l3
    l3.reverse()
    return l3

# def getList(n):
#     head = Node(0)
#     current = head
#     for i in xrange(1, n):

#         current.next = Node(i)

#         current = current.next

#     return LinkedList(head)

# ll = getList(5)

# ll.print_linked_list()


# head = Node(1)
# ll = LinkedList(head, head)
# ll.insert(Node(2))
# ll.insert(Node(3))
# ll.print_linked_list()
# ll.reverse()
# ll.print_linked_list()

head = Node(9)
l1 = LinkedList(head, head)
l1.insert(Node(9))

head2 = Node(9)
l2 = LinkedList(head2, head2)

# l1.print_linked_list()
# l2.print_linked_list()

l3 = add_two_linked_lists(l1, l2)
l3.print_linked_list()

# 123 + 456

# head = Node(1)
# l1 = LinkedList(head, head)
# l1.insert(Node(2))
# l1.insert(Node(3))
#
# head2 = Node(4)
# l2 = LinkedList(head2, head2)
# l2.insert(Node(5))
# l2.insert(Node(6))
#
# l3 = add_two_linked_lists(l1, l2)
# l3.print_linked_list()

# 123 + 456

# 1->2->3->4

#    4->5->6

# 1  6  9  0

# 4 -> 2 -> 3 -> 1

# 6 -> 5 -> 4

# 0 -> 9 -> 6 -> 1

# reverse both linked lists

# define a third linked list

# sum each corresponding value
# making sure to keep track of carry-over

# reverse the third linked list

# carry over is 1

# 1 -> 6 -> 9 -> 0
