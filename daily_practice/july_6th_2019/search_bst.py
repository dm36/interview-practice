class BST():
    def __init__(self, root):
        self.root = root

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, node):
    if not root:
        root = node
    # going left
    if node.value < root.value:
        if not root.left:
            root.left = node
            return
        else:
            insert(root.left, node)
            return
    # going right
    elif node.value > root.value:
        if not root.right:
            root.right = node
            return
        else:
            insert(root.right, node)
            return

def isPresent(root, val):
    if not root:
        return 0
    elif val == root.value:
        return 1
    elif val < root.value:
        if not root.left:
            return 0
        else:
            return isPresent(root.left, val)
    elif val > root.value:
        if not root.right:
            return 0
        else:
            return isPresent(root.right, val)
