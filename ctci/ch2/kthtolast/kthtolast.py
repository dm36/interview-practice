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
        temp = self.head
        arrOfNodes = [temp.data]

        while temp.next != None:
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

    def len(self):
        temp = self.head
        count = 0

        while temp != None:
            count += 1
            temp = temp.next

        return count

    # k = 0 is the last element the way this is implemented
    def kthtolast(self, k):
        temp = self.head
        count = self.len() - k - 1
        print count

        while count != 0:
            temp = temp.next
            count -= 1

        return temp.data


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getNext(self):
        return self.next

    def data(self):
        return self.data


data = LinkedList(Node(5)).head.data
print "Data for the head is:", data

linked_list = LinkedList(Node(5))
linked_list.add(Node(5))
linked_list.add(Node(5))
linked_list.add(Node(6))
linked_list.add(Node(6))
linked_list.add(Node(4))
linked_list.str()

print linked_list.kthtolast(0)


# print "Data for the node at the end of the linked list is: ", linked_list.getHead().getNext().getNext().data
