class Stack():
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.insert(0, item)

    def pop(self):
        return self.stack.pop(0)

    def len(self):
        return len(self.stack)

def number_of_items(string):
    stack = Stack()
    count = 0

    for char in string:
        if char == '[':
            stack.push(']')
        if char == '(':
            stack.push(')')
        if char == ')':
            if stack.len() == 0 or stack.pop() != char:
                return -1
            count += 1
        if char == ']':
            if stack.len() == 0 or stack.pop() != char:
                return -1
            count += 1
    return count

string = "here is an [(example)]"
print number_of_items(string)

string2 = "here is an (example]"
print number_of_items(string2)

string3 = "here is an )example("
print number_of_items(string3)

string4 = "here is an []"
print number_of_items(string4)

string5 = "here is an [ex(am)ple]"
print number_of_items(string5)

# Create a function that returns the number of item
#  - JS String
#  - (, ), [, ],
#  - "here is an (example)" 1
#  - -1
#
#  Input: "here is an [(example)]" => 2
#  Input: "here is an (example]" => -1
#  Input: "here is an )example(" => -1
#  Input: "here is an []" => 1
#  Input: "here is an [ex(am)ple]" => 2
#  */
