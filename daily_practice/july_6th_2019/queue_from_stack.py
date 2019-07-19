class Stack():
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def len(self):
        return len(self.stack)

    def peek(self):
        len = self.len()
        return self.stack[len - 1]

my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
print my_stack.peek()
print my_stack.pop()
print my_stack.peek()

class Queue():
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    # to push just add to stack1
    def push(self, item):
        self.stack1.push(item)

    # same idea as peek
    def pop(self):
        while self.stack1.len():
            self.stack2.push(self.stack1.pop())

        return self.stack2.pop()

        while self.stack2.len():
            self.stack1.push(self.stack2.pop())

    # pop items from stack1 and push each item
    # onto stack2 (thereby reversing the contents of stack1
    # in stack2)- peek from stack2

    # then to clean up push contents of stack2 => stack1
    def peek(self):
        while self.stack1.len():
            self.stack2.push(self.stack1.pop())

        print self.stack2.peek()

        while self.stack2.len():
            self.stack1.push(self.stack2.pop())

my_queue = Queue()
my_queue.push(1)
my_queue.push(2)
my_queue.push(3)
my_queue.push(4)
my_queue.peek()
print my_queue.pop()
my_queue.peek()
