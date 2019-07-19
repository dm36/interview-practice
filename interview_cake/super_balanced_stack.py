class Stack():
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.insert(0, item)
    def pop(self):
        return self.stack.pop(0)
    def len(self):
        return len(self.stack)

# Each time we hit a leaf with a new depth, there are two ways that our tree might now be unbalanced:
#
# There are more than 2 different leaf depths- if there are more than 2
# different leaf depths they have to be more than one apart

# There are exactly 2 leaf depths and they are more than 1 apart.
class BinaryTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

# class Node():
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
# class BST():
#     def __init__(self, root):
#         self.root = root
#
#     def insert_left(self, node):
#         self.root.left = node
#         return self.root.left
#
#     def insert_right(self, node):
#         self.root.right = node
#         return self.root.right

def is_balanced(root):
    stack = Stack()
    stack.push((root, 0))
    leaf_depths = []

    while stack.len() > 0:
        node, depth = stack.pop()
        if not node.left and not node.right:
            if depth not in leaf_depths:
                leaf_depths.append(depth)
                if len(leaf_depths) > 2 or (len(leaf_depths) == 2 and abs(leaf_depths[1] - leaf_depths[0]) > 1):
                    return False
        if node.left:
            stack.push((node.left, depth + 1))
        if node.right:
            stack.push((node.right, depth + 1))

    return True

# bst = BST(Node(5))
# bst.insert_left(Node(3))
# bst.insert_right(Node(8))
#
# print bst.root.value
# print bst.root.left.value
# print bst.root.right.value
#
# print is_balanced(bst.root)
#
# tree = BST(Node(5))
# left = tree.insert_left(Node(8))
# right = tree.insert_right(Node(6))
# left.insert_left(Node(1))
# left.insert_right(Node(2))
# right.insert_left(Node(3))
# right.insert_right(Node(4))
# result = is_balanced(tree)
# print result

tree = BinaryTreeNode(5)
left = tree.insert_left(8)
right = tree.insert_right(6)
left.insert_left(1)
left.insert_right(2)
right.insert_left(3)
right.insert_right(4)
result = is_balanced(tree)
print result
