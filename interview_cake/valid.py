# Want BST to have a root, we'll be
# passing Nodes to init
class BST():
    def __init__(self, node):
        self.root = node

# Want node to have a value and a left and right
# subtree pointing to None
class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# We call insert on the root of a BST
# if there's a left recurse on the left, otherwise
# set this node to be the left, same idea on the right
def insert(root, node):
    if node.value < root.value:
        if root.left == None:
            root.left = node
        else:
            insert(root.left, node)
    else:
        if root.right == None:
            root.right = node
        else:
            insert(root.right, node)

# To check if a bst is valid- we'll be bounding
# each node in limits based on values of its parents
def valid(root):
    return valid_helper(root, -float("inf"), float("inf"))

def valid_helper(root, low, high):
    if root == None:
        return True
    elif not low < root.value < high:
        return False
    else:
        return valid_helper(root.left, low, root.value) and valid_helper(root.right, root.value, high)


bst = BST(Node(6))
insert(bst.root, Node(3))
insert(bst.root, Node(10))
print bst.root.left.value
print bst.root.right.value

print valid(bst.root)

bst2 = BST(Node(20))
insert(bst.root, Node(3))
insert(bst.root, Node(10))
print bst.root.left.value
print bst.root.right.value
