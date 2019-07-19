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
        return final_str

    def len(self):
        temp = self.head
        count = 0

        while temp != None:
            count += 1
            temp = temp.next

        return count

    def reverse(self):
        temp = self.head
        after = None
        before = None

        print "Before reverse is: "
        before_reverse = self.str()

        while temp != None:
            after = temp.next
            temp.next = before
            before = temp
            temp = after

        # temp is none and before is the last node in the
        # linked list
        self.head = before
        print "After reverse is: "
        after_reverse = self.str()

        if before_reverse == after_reverse:
            return True
        else:
            return False

    # Thought is reverse the linked list and check if str of the reversed
    # linked list is equal to str of the linked list
    def palindrome(self):
        linked_list_reverse = self.reverse()
        return linked_list_reverse

    def palindrome_other(self):
        temp = self.head
        arr = []

        while temp != None:
            arr.append(temp.data)
            temp = temp.next

        before_arr = arr
        after_arr = list(arr)
        after_arr.reverse()

        if before_arr == after_arr:
            return True
        else:
            return False

    # k = 0 is the last element the way this is implemented
    def kthtolast(self, k):
        temp = self.head
        count = self.len() - k - 1

        while count != 0:
            temp = temp.next
            count -= 1

        return temp.data

    # https://cs.stackexchange.com/questions/10360/floyds-cycle-detection-algorithm-determining-the-starting-point-of-cycle
    def loopDetection(self):
        walker = self.head
        runner = self.head.next

        while walker != runner:
            walker = walker.next
            runner = runner.next.next

        return walker.data

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getNext(self):
        return self.next

    def data(self):
        return self.data


data = LinkedList(Node(5)).head.data
print "The head's data is: ", data
print ""

print "Testing the str function: "
linked_list = LinkedList(Node(5))
linked_list.add(Node(5))
linked_list.add(Node(5))
linked_list.add(Node(6))
linked_list.add(Node(6))
linked_list.add(Node(4))
linked_list.str()
print ""

print "Testing kth to last: "
print linked_list.kthtolast(0)
print ""

print "Testing palindrome: "
nodeA = Node("A")
linked_list2 = LinkedList(nodeA)

nodeB = Node("B")
linked_list2.add(nodeB)

nodeC = Node("C")
linked_list2.add(nodeC)

nodeD = Node("D")
linked_list2.add(nodeD)

nodeE = Node("E")
linked_list2.add(nodeE)

print "Array reverse test: ", linked_list2.palindrome_other()
print ""
print linked_list2.palindrome()
print ""

print "Testing palindrome: "

nodeA2 = Node("A")
linked_list3 = LinkedList(nodeA2)

nodeB2 = Node("B")
linked_list3.add(nodeB2)

nodeB3 = Node("B")
linked_list3.add(nodeB3)

nodeA3 = Node("A")
linked_list3.add(nodeA3)

print "Array reverse test: ", linked_list3.palindrome_other()
print ""
print linked_list3.palindrome()
