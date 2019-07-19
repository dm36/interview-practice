class BST():
    def __init__(self, root):
        self.root = root

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # def insert_left(self, value):
    #     self.left = Node(value)
    #     return self.left
    #
    # def insert_right(self, value):
    #     self.right = Node(value)
    #     return self.right

def insert(root, node):
    if not root:
        root = node
    else:
        if node.value < root.value:
            if not root.left:
                root.left = node
            else:
                insert(root.left, node)
        if node.value > root.value:
            if not root.right:
                root.right = node
            else:
                insert(root.right, node)

def preorder(root, arr):
    if root:
        arr.append(root.value)
        preorder(root.left, arr)
        preorder(root.right, arr)

def inorder(root, arr):
    if root:
        inorder(root.left, arr)
        arr.append(root.value)
        inorder(root.right, arr)

def range_sum_bst(root, L, R):
    arr = []
    preorder(root, arr)
    return sum([node for node in arr if node >= L and node <= R])

bst = BST(Node(10))
insert(bst.root, Node(5))
insert(bst.root, Node(15))
insert(bst.root, Node(3))
insert(bst.root, Node(7))
insert(bst.root, Node(18))

preorder(bst.root, [])
inorder(bst.root, [])

print range_sum_bst(bst.root, 7, 15)
