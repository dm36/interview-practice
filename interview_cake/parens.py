class Stack():
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.insert(0, item)
    def pop(self):
        return self.stack.pop(0)

# If you see a '(' push the index in the sentence at which you saw
# that open paren

# If you see a ')'- pop from the stack and check to see if that
# index is open position- if it is return the index of that ')'

# Best understood with an example:
# In the below example:
# (, push 10
# (, push 28
# ), pop 28- 28's not 10 so we keep going
# ...
# until you see the matching ) for the ( at 10-
# and then the index of that ) i.e. 79!

# def find_close_paren(sentence, open_position):
#     stack = Stack()
#     for i in range(len(sentence)):
#         if sentence[i] == '(':
#             print i
#             stack.push(i)
#         elif sentence[i] == ')':
#             start_pos = stack.pop()
#             if start_pos == open_position:
#                 return i

# O(n) runtime, O(1) space- using a count rather than a stack
# Start 1 past the location of the open paren we're looking to match
# See a (- increment count
# See a )- check if count is 0 (this indicates that this is the matching
# paren for our paren at open_position) and if so return i, otherwise
# decrement count by 1
def find_close_paren(sentence, open_position):
    count = 0
    for i in range(open_position + 1, len(sentence)):
        if sentence[i] == '(':
            count += 1
        elif sentence[i] == ')':
            if count == 0:
                return i
            else:
                count -= 1

sentence = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
print sentence
result = sentence.index("(")
print result

print find_close_paren(sentence, result)
