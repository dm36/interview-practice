"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
    if head == None:
        return False

    runner = head
    walker = head.next
    count = 0

    while walker != runner:
        if walker == None or walker.next == None:
            return False

        walker = walker.next
        runner = runner.next.next

    return True
