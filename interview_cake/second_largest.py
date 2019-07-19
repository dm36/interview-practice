class BST():
    def __init__(self, root):
        self.root = root

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, node):
    if root:
        if node.value < root.value:
            if not root.left:
                root.left = node
            else:
                insert(root.left, node)
        else:
            if not root.right:
                root.right = node
            else:
                insert(root.right, node)
    else:
        root = node

def second_largest(root):
    node = root
    parent = None
    while node.right != None:
        parent = node
        node = node.right
    return parent.value

bst = BST(Node(5))
insert(bst.root, Node(6))
insert(bst.root, Node(3))
insert(bst.root, Node(4))
insert(bst.root, Node(8))

print bst.root.value
print bst.root.left.value
print bst.root.left.right.value
print bst.root.right.value
print bst.root.right.right.value

print "The second largest node is: ", second_largest(bst.root)
