import unittest

class Stack():
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.len() == 0:
            return None
        return self.stack.pop()

    def len(self):
        return len(self.stack)

    def peek(self):
        if self.len() == 0:
            return None
        return self.stack[-1]

class MaxStack():
    def __init__(self):
        self.stack = Stack()
        self.max_stack = Stack()

    def push(self, item):
        self.stack.push(item)

        # if item is greater than or equal to the
        # top item on the max stack- push this new item
        # onto the stack
        if self.max_stack.peek() is None or item >= self.max_stack.peek():
            self.max_stack.push(item)

    def pop(self):
        # if the popped item is equal to the max item on the stack
        # => pop off the max stack too
        item = self.stack.pop()
        if item == self.max_stack.peek():
            self.max_stack.pop()

        return item

    def len(self):
        return self.stack.len()

    def peek(self):
        return self.stack.peek()

    def get_max(self):
        return self.max_stack.peek()

# max_stack = MaxStack()
# max_stack.push(5)
# max_stack.push(10)
# max_stack.push(3)

class Test(unittest.TestCase):

    def test_stack_usage(self):
        max_stack = MaxStack()

        max_stack.push(5)

        actual = max_stack.get_max()
        expected = 5
        self.assertEqual(actual, expected)

        max_stack.push(4)
        max_stack.push(7)
        max_stack.push(7)
        max_stack.push(8)

        actual = max_stack.get_max()
        expected = 8
        self.assertEqual(actual, expected)

        actual = max_stack.pop()
        expected = 8
        self.assertEqual(actual, expected)

        actual = max_stack.get_max()
        expected = 7
        self.assertEqual(actual, expected)

        actual = max_stack.pop()
        expected = 7
        self.assertEqual(actual, expected)

        actual = max_stack.get_max()
        expected = 7
        self.assertEqual(actual, expected)

        actual = max_stack.pop()
        expected = 7
        self.assertEqual(actual, expected)

        actual = max_stack.get_max()
        expected = 5
        self.assertEqual(actual, expected)

        actual = max_stack.pop()
        expected = 4
        self.assertEqual(actual, expected)

        actual = max_stack.get_max()
        expected = 5
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)




# class Stack(object):
#     def __init__(self):
#         """Initialize an empty stack"""
#         self.items = []
#         self.max = -float("inf")
#         self.second_max = -float("inf")
#
#     def push(self, item):
#         """Push a new item onto the stack"""
#
#         # if the pushed item is greater than self.max
#         # update second max to be max and max to be the pushed
#         # item
#         if item > self.max:
#             self.second_max = self.max
#             self.max = item
#
#         # if the pushed item is greater than self.second_max
#         # but not self.max => update self.second_max to the
#         # item
#         elif item > self.second_max and item < self.max:
#             self.second_max = item
#
#         self.items.append(item)
#
#     def pop(self):
#         """Remove and return the last item"""
#         # If the stack is empty, return None
#         # (it would also be reasonable to throw an exception)
#         if not self.items:
#             return None
#
#         # if the item being popped is the max
#         # update max to be second_max- but what would second_max now be??
#         item = self.items.pop()
#         if item == self.max:
#             self.max = self.second_max
#
#         # if the item being popped is the second max
#         # how would we update second_max???
#         if item == self.second_max:
#
#         return self.items.pop()
#
#     def peek(self):
#         """Return the last item without removing it"""
#         if not self.items:
#             return None
#         return self.items[-1]

# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)

# get_max() returns the largest element in the stack
# should not remove the item

# could walk through the stack- find the max and return that

# could keep track of the max value on the stack

# whenever you push an item- compare this to the max value
# and update if this value is greater

# whenever you pop an item- if you pop the max- so should
# always keep track of the second max too

# two stacks within maxstack class- stack holds all integers- and
# maxes stack holds all maxima

# maxes stack to keep our max up to date in constant time as
# we push and pop

# whenever we push an item- check to see if it's greater than
# or equal to the current max- top of maxes_stack

# if so push it onto maxes_stack

# when we pop- pop() from the top of maxes_stack if the item
# equals the top item in maxes_stack

# requires O(m) additional space for the additional stack
# solution that requires O(1) additional space?

# spending time on push() and pop() so we can save time
# on get_max() => optimize for time cost of calls to get_max()

# could have chosen to optimize on something else-
# running push() and pop() frequently and running get_max()

# could have optimized for faster push() and pop() methods
# decide what we're optimizing for
