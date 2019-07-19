class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def isEmpty(self):
        return len(self.stack) == 0


my_stack = Stack()
my_stack.push(5)
my_stack.push(10)
my_stack.push(3)
my_stack.push(4)

print "The top element is", my_stack.peek()

popped = my_stack.pop()
print "Popped: ", popped

print "The top element is", my_stack.peek()

popped = my_stack.pop()
print "Popped: ", popped

print "The top element is", my_stack.peek()

popped = my_stack.pop()
print "Popped: ", popped

print "The top element is", my_stack.peek()

print my_stack.isEmpty()
