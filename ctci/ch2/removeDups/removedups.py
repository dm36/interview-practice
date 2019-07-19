# import pdb; pdb.set_trace()
class LinkedList:
    def __init__(self, head):
        self.head = head

    def getHead(self):
        return self.head

    def add(self, node):
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = node

    def delete(self, node):
        temp = self.head
        while temp != None:
            if temp.next.data == node.data:
                temp.next = temp.next.next
                return
            temp = temp.next

    def removeDups(self):
        arrOfNodes = []

        temp = self.head
        while temp != None:
            if temp.data in arrOfNodes:
                self.delete(temp)
            else:
                arrOfNodes.append(temp.data)
            temp = temp.next

    # 5 -> 5 -> 4 logic
    # 1) temp = 5, arrOfNodes = [5], temp.next.data = 5
    # is in arrOfNodes = [5], so go into if, temp.next now = 4
    # 2) temp = 5, arrOfNodes = [5], temp.next.data = 4 not in arrOfNodes
    # so hit else case, arrOfNodes = [5, 4], temp = 4
    # 3) temp = 4, temp.next = None so break out of while loop w/
    #    5 -> 4 as our linked list
    def removeDupsNoDelete(self):
        # set to the temp to the head- have the data from temp be in the
        # array of nodes
        temp = self.head
        arrOfNodes = [temp.data]

        # as long as temp has a next (so we stop at the tail of the linked list)
        while temp.next:
            if temp.next.data in arrOfNodes:
                temp.next = temp.next.next
            else:
                arrOfNodes.append(temp.next.data)
                temp = temp.next

    def removeDupsEfficient(self):
        walker = self.head

        while walker != None:
            runner = walker.next
            while runner != None:
                if walker.data == runner.data:
                    self.delete(runner)
                    break
                runner = runner.next

            walker = walker.next

    def removeDupsNoDeleteEfficient(self):
        walker = self.head
        while walker.next:
            runner = walker.next
            while runner:
                if walker.data == runner.data:
                    walker.next = walker.next.next
                    break
                else:
                    walker = walker.next
                    runner = walker.next

    def str(self):
        temp = self.head
        final_str = ""
        while temp != None:
            if temp.next == None:
                final_str += str(temp.data)
            else:
                final_str += str(temp.data) + "->"
            temp = temp.next
        print final_str

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getNext(self):
        return self.next

    def data(self):
        return self.data


data = LinkedList(Node(5)).head.data
print "The head's data is:", data

linked_list = LinkedList(Node(5))
linked_list.add(Node(5))
linked_list.add(Node(5))
linked_list.add(Node(6))
linked_list.add(Node(6))
linked_list.add(Node(4))

linked_list.delete(Node(4))
linked_list.str()

# linked_list.removeDups()
# linked_list.str()

# linked_list.removeDupsNoDelete()
# linked_list.str()

# linked_list.removeDupsEfficient()
# linked_list.str()

linked_list.removeDupsNoDeleteEfficient()
linked_list.str()
