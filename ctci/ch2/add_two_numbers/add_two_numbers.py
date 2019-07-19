class LinkedList():
    def __init__(self, node):
        self.head = node

    def add(self, node):
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = node

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

# One option is appending all digits of the ll to an array- reversing
# the array and then converting the arr of digits into a single number
def add_two_numbers(l1, l2):
    arr1 = []
    arr2 = []
    while l1 != None:
        arr1.append(l1.data)
        l1 = l1.next

    while l2 != None:
        arr2.append(l2.data)
        l2 = l2.next

    arr1.reverse()
    print arr1

    arr2.reverse()
    print arr2

    num_1 = 0
    num_2 = 0

    # With [3, 4, 2] I want to start at the 2
    # multiplied by (10 * 0), then I want to add that to 4
    # multiplied by (10 * 1), then I want to add that to
    # 3 multiplied by (10 * 2)
    for i in range(len(arr1)-1, -1, -1):
        num_1 += arr1[i] * (10 ** (len(arr1) - i - 1))
        num_2 += arr2[i] * (10 ** (len(arr2) - i - 1))

    return num_1 + num_2

l1 = LinkedList(Node(2))
l1.add(Node(4))
l1.add(Node(3))

l2 = LinkedList(Node(5))
l2.add(Node(6))
l2.add(Node(4))

print add_two_numbers(l1.head, l2.head)
