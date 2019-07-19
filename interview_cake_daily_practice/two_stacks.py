# class Stack():
#     def __init__(self):
#         self.stack = []
#     def push(self, item):
#         self.stack.insert(0, item)
#     def pop(self):
#         return self.stack.pop(0)
#     def len(self):
#         return len(self.stack)
#
# # class Queue():
# #     def __init__(self):
# #         self.stack1 = Stack()
# #         self.stack2 = Stack()
# #
# #     # Push onto the first stack
# #     def enqueue(self, item):
# #         self.stack1.push(item)
# #
# #     # Pop everything from stack1 onto stack2 and then pop
# #     # from stack2
# #
# #     # So say we pushed a, b and c onto the stack:
# #     # We would have:
# #     #  "c"
# #     #  "b"
# #     #  "a"
# #
# #     # so if we popped from this stack- we would expect to get c.
# #     # However- we're trying to build a queue NOT a stack. So- let's
# #     # pop everything onto stack2:
# #
# #     # "a"
# #     # "b"
# #     # "c"
# #
# #     # Now if we dequeue- we would get "a"- as desired- in a queue- we want
# #     # the first dequeued item to be the first item we added to the queue
# #
# #     # But we also want stack1 to be in its og state so future enqueue
# #     # operations work
# #     def dequeue(self):
# #         while self.stack1.len():
# #             self.stack2.push(self.stack1.pop())
# #
# #         elem = self.stack2.pop()
# #         while self.stack2.len():
# #             self.stack1.push(self.stack2.pop())
# #         return elem

class QueueTwoStacks(object):
    def __init__(self):
        self.in_stack  = []
        self.out_stack = []

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if len(self.out_stack) == 0:
            # Move items from in_stack to out_stack, reversing order
            while len(self.in_stack) > 0:
                newest_in_stack_item = self.in_stack.pop()
                self.out_stack.append(newest_in_stack_item)

        # If out_stack is still empty, raise an error
        if len(self.out_stack) == 0:
            raise IndexError("Can't dequeue from empty queue!")

        # If the length of the output stack is > 0- just start popping
        # otherwise we have to reverse elements on the in stack and then
        # pop
        return self.out_stack.pop()

# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
#
# stack2 = Stack()
# stack2.push(5)
# stack2.push(6)
# stack2.push(7)
# stack2.push(8)

# two_stacks = Queue()
# two_stacks.enqueue("a")
# two_stacks.enqueue("b")
# two_stacks.enqueue("c")
# print two_stacks.dequeue()

two_stacks = QueueTwoStacks()
two_stacks.enqueue("a")
two_stacks.enqueue("b")
two_stacks.enqueue("c")
print two_stacks.dequeue()


# Length of stack
# print stack.len()
# print
#
# # Making sure we are behaving like a stack (LIFO)
# print stack.pop()
# print stack.pop()
# print stack.pop()
# print stack.pop()
