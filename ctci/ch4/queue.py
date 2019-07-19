class Queue:
    def __init__(self):
        self.queue = []
    def add(self, item):
        self.queue.append(item)
    def remove(self):
        return self.queue.pop(0)
    def peek(self):
        return self.queue[0]
    def isEmpty(self):
        return len(self.queue) == 0

# queue = Queue()
# queue.add(10)
# queue.add(5)
# queue.add(6)
# queue.add(3)
#
# print "The top of the queue is", queue.peek()
#
# queue.remove()
# print "The top of the queue is", queue.peek()
#
# queue.remove()
# print "The top of the queue is", queue.peek()
#
# queue.remove()
# print "The top of the queue is", queue.peek()
#
# print queue.isEmpty()
