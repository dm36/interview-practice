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

#      10
#   |     |
#   5     12

def valid_helper(root, low, high):
    # if root is less than the value of the lower or greater than the
    # uppper bound => return False
    if not root:
        return True

    if root.value < low or root.value > high:
        return False

    # when we go left => upper bounded by the value of the root node
    # when we go right => lower bounded by the value of the root node
    return valid_helper(root.left, low, root.value) and valid_helper(root.right, root.value, high)

def valid_bst(root):
    return valid_helper(root, -float("inf"), float("inf"))

root = Node(10)
bst = BST(root)
print bst.root.value

insert(root, Node(5))
insert(root, Node(3))
insert(root, Node(11))
insert(root, Node(15))

print valid_bst(root)

print bst.root.left.value
print bst.root.left.left.value
print bst.root.right.value
print bst.root.right.right.value

new_root = Node(11)
new_root.left = Node(12)
print valid_bst(new_root)
