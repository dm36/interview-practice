def insertNodeAtPosition(head, data, position):
    count = 0
    node = head
    while count < position - 1:
        node = node.next
        count += 1

    temp = node.next
    current_node = SinglyLinkedListNode(data)
    node.next = current_node
    current_node.next = temp
