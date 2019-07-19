class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def recoverFromPreorder(S):
    # initialize stack to an empty list, and i to 0
    stack, i = [], 0
    # as long as there is more in the input string "1-2--3--4-5--6--7"
    while i < len(S):
        level, val = 0, "" # initialize level to be 0 and val to be "" after
        # every iteration of the while loop

        # as long as there are dashes
        # increment level and i
        while i < len(S) and S[i] == '-':
            level, i = level + 1, i + 1

        # while there are not dashes increment the value of val
        # i increment is a little odd but it's incrementing i over by the
        # value of the node
        while i < len(S) and S[i] != '-':
            val, i = val + S[i], i + 1

        # size of the stack bigger than level of node- pop
        # stack until its not
        while len(stack) > level:
            stack.pop()

        # build a TreeNode of the val
        node = TreeNode(val)

        # if there's a stack and the last element on the stack
        # has no left child- set the node to be the left child
        # of this last element on the stack
        # otherwise set it to be the right child

        if stack and stack[-1].left is None:
            stack[-1].left = node
        elif stack:
            stack[-1].right = node

        # add the node to the stack
        stack.append(node)

    # return the first element in the stack
    return stack[0]

print recoverFromPreorder("1-2--3--4-5--6--7")

# For node 1
# Starting out there are no dashes so we go straight to the second while loop
# after the second while loop val will be 1, i would be 1
# add node 1 to the stack

# For node 2
# level would be set to 1, i would be 2 after first while loop
# val would be set to 2, i would be set to 3 after second while loop

# len(stack) = 1, level is also 1 so we don't pop anything from the stack
# build a TreeNode of 2, make 2 the left of 1 and add it to the stack

# For node 3
# first while loop
# level would be set to 2 because of the two dashes before the 3
# i would be updated to be at the 3

# second while loop/after
# val would become 3, i would point to the - after 3, len(stack) would be 2, level
# would also be 2, so we would form a TreeNode from 3 and set it to 2's left
