class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.insert(0, item)
    def pop(self):
        return self.stack.pop(0)
    def len(self):
        return len(self.stack)

def bracket_validator(my_string):
    stack = Stack()
    for char in my_string:
        if char == '{':
            stack.push('}')
        elif char == '[':
            stack.push(']')
        elif char == '(':
            stack.push(')')
        elif char in [']', '}', ')']:
            if char != stack.pop():
                return False
    return stack.len() == 0

print bracket_validator("{[]()}")
print bracket_validator("{[}")
print bracket_validator("{[(])}")
