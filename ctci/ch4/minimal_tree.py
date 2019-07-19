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

arr = [1, 2, 3, 4, 5, 6, 7]
node = minBinarySearchTree(arr, 0, len(arr)-1)
print node.value
print node.left.value
print node.left.left.value
print node.left.right.value
print node.right.value
print node.right.left.value
print node.right.right.value
