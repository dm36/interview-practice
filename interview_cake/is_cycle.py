class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

# O(n) time, O(1) space
def contains_cycle(head):
    walker = head
    runner = head.next

    while runner.next != None:
        if walker == runner:
            return True
        walker = walker.next
        runner = runner.next.next
    return False

# O(n) time, O(n) space
def contains_cycle_set(head):
    my_set = set()
    while head != None:
        if head in my_set:
            return True
        my_set.add(head)
        head = head.next
    return False


a = Node('A')
b = Node('A')
c = Node('C')

a.next = b
b.next = a

print a.next.data
print b.next.data

print contains_cycle(a)
print contains_cycle_set(a)


d = Node('D')
e = Node('E')
f = Node('F')
g = Node('G')

d.next = e
e.next = f
f.next = g

print d.next.next.data

print contains_cycle(d)
print contains_cycle_set(d)
