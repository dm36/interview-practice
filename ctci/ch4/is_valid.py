class BST():
    def __init__(self, root):
        self.root = root

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, node):
    if root:
        if node.value < root.value:
            if root.left:
                insert(root.left, node)
            else:
                root.left = node
        if node.value > root.value:
            if root.right:
                insert(root.right, node)
            else:
                root.right = node
    else:
        root = node

def search(root, node):
    if root == None:
        return
    if node.value == root.value:
        return True
    elif node.value < root.value:
        return search(root.left, node)
    else:
        return search(root.right, node)

def preorder(root):
    if root != None:
        print (root.value)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root != None:
        postorder(root.left)
        postorder(root.right)
        print (root.value)

def inorder(root):
    if root != None:
        inorder(root.left)
        print (root.value)
        inorder(root.right)


def minBinarySearchTree(arr, start, end):
    if start > end:
        return
    mid = (start + end) / 2
    node = Node(arr[mid])
    node.left = minBinarySearchTree(arr, start, mid - 1)
    node.right = minBinarySearchTree(arr, mid + 1, end)
    return node

def isValid(root):
    return isValidHelper(root, -float("inf"), float("inf"))

def isValidHelper(root, lower, upper):
    if root == None:
        return True
    if root.value < lower or root.value > upper:
        return False

    leftValid = isValidHelper(root.left, lower, root.value)
    rightValid = isValidHelper(root.right, root.value, upper)
    return leftValid and rightValid

bst = BST(Node(5))
insert(bst.root, Node(3))
insert(bst.root, Node(7))
insert(bst.root, Node(2))
insert(bst.root, Node(4))
insert(bst.root, Node(6))
insert(bst.root, Node(8))

print isValid(bst.root)

bst2 = BST(Node(5))
insert(bst2.root, Node(3))
insert(bst2.root, Node(2))

print isValid(bst2.root)

bst3 = BST(Node(6))
print isValid(bst3.root)

bst4 = BST(Node(5))
insert(bst4.root, Node(6))
insert(bst4.root, Node(8))
print isValid(bst4.root)

bst5 = BST(Node(5))
insert(bst5.root, Node(3))
insert(bst5.root, Node(7))
insert(bst5.root, Node(6))
insert(bst5.root, Node(8))
print isValid(bst5.root)
