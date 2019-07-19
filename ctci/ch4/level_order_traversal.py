from queue import Queue
import collections

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

def height(root):
    if root == None:
        return 0
    return 1 + max(height(root.left), height(root.right))

def isBalanced(root):
    if root.left == None and root.right == None:
        return True

    left_height = height(root.left)
    right_height = height(root.right)

    if abs(left_height - right_height) > 1:
        return False

    balanced_left = isBalanced(root.left)
    balanced_right = isBalanced(root.right)

    return balanced_left and balanced_right

# Add root node to the queue
# While the queue is not empty, remove the node from the queue, print
# it and add its children (if it has any)
def level_order_traversal(root):
    level_queue = Queue()
    level_queue.add((root, 0))
    dist_map = collections.defaultdict(list)

    while not level_queue.isEmpty():
        node = level_queue.remove()
        dist_map[node[1]].append(node[0].value)
        if node[0].left:
            level_queue.add((node[0].left, node[1] + 1))
        if node[0].right:
            level_queue.add((node[0].right, node[1] + 1))
    return dist_map.values()

bst = BST(Node(5))
insert(bst.root, Node(3))
insert(bst.root, Node(7))
insert(bst.root, Node(6))
insert(bst.root, Node(8))
insert(bst.root, Node(2))
insert(bst.root, Node(4))
level_order_traversal(bst.root)
print

bst2 = BST(Node(5))
insert(bst2.root, Node(3))
insert(bst2.root, Node(2))
level_order_traversal(bst2.root)
print
#
# bst3 = BST(Node(6))
# level_order_traversal(bst3.root)
# print
#
# bst4 = BST(Node(5))
# insert(bst4.root, Node(6))
# insert(bst4.root, Node(8))
# level_order_traversal(bst4.root)
# print
#
# bst5 = BST(Node(5))
# insert(bst5.root, Node(3))
# insert(bst5.root, Node(7))
# insert(bst5.root, Node(6))
# insert(bst5.root, Node(8))
# level_order_traversal(bst5.root)
# print
