# LinkedList defined by a head
class LinkedList():
    def __init__(self, head):
        self.head = head

    # insert
    def insert(self, node):
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node

    # two ways to do this:
    # either you have a walker and a runner- have the runner be k steps ahead
    # and return the walker

    # get the length of the linked list and then iterate length - k times
    def len(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def kth_to_last(self, k):
        len = self.len()
        if k > len:
            raise Exception('k must be less than the length of the linked list')

        count = self.len() - k
        temp = self.head

        while count:
            temp = temp.next
            count -= 1

        return temp

    def is_cycle(self):
        

    # def kth_to_last_node(k, head):
    #     # Find the length of the linked list
    #     temp = head
    #     length = 0
    #
    #     while temp:
    #         temp = temp.next
    #         length += 1
    #
    #     if k > length:
    #         raise Exception('k must be less than the length of the linked list')
    #
    #     # Iterate length - k times and return that node
    #     count = length - k
    #     temp = head
    #
    #     while count:
    #         temp = temp.next
    #         count -= 1
    #
    #     return temp

    # def reverse(self):

# Node defined by a value and a pointer to a next node
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

ll = LinkedList(Node(1))
ll.insert(Node(2))
ll.insert(Node(3))

print (ll.len())
print ll.kth_to_last(3).value
print ll.kth_to_last(2).value
print ll.kth_to_last(1).value

# print ll.head.value
# print ll.head.next.value
# print ll.head.next.next.value
