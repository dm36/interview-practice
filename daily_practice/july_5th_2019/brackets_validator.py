# define a stack

# and everytine we observe an opening character
# we push the corresponding closing character onto the stack

# everytime we observe a closing character- we pop- and check to see
# if the characters tally up

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def len(self):
        return len(self.stack)

def is_valid(input):
    stack = Stack()
    open_to_close = {'{' : '}', '[' : ']', '(' : ')'}

    for char in input:
        if char in open_to_close.keys():
            stack.push(open_to_close[char])

        elif char in open_to_close.values():
            if stack.len() == 0 or char != stack.pop():
                return False

    return stack.len() == 0

print is_valid("{[]()}")
print is_valid("{[(])}")
print is_valid("{[}")
print is_valid('[[]()')
