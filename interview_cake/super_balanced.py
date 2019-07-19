class BST:
    def __init__(self, root):
        self.root = root

    def inorder(self):
        if self.root:
            inorder(self.root.left)
            print self.root.value
            inorder(self.root.right)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, node):
    if not root:
        root = node
        return
    elif node.value <= root.value:
        if not root.left:
            root.left = node
            return
        else:
            insert(root.left, node)
            return
    elif node.value > root.value:
        if not root.right:
            root.right = node
            return
        else:
            insert(root.right, node)
            return


# go to every leaf in the bst
def super_balanced(root):
    depth_array = []
    super_balanced_helper(root, 0, depth_array)
    print depth_array
    depth_array.sort()
    if depth_array[-1] - depth_array[0] > 1:
        return False
    else:
        return True

def super_balanced_helper(root, depth, depth_array):
    if not root.left and not root.right:
        depth_array.append(depth)
        return
    if root.left:
        super_balanced_helper(root.left, depth + 1, depth_array)
    if root.right:
        super_balanced_helper(root.right, depth + 1, depth_array)

bst = BST(Node(5))
insert(bst.root, Node(3))
insert(bst.root, Node(4))
insert(bst.root, Node(6))
print bst.root.value
print bst.root.left.value
print bst.root.left.right.value
print bst.root.right.value

super_balanced(bst.root)

bst2 = BST(Node(17))
insert(bst2.root, Node(13))
insert(bst2.root, Node(10))
insert(bst2.root, Node(15))
insert(bst2.root, Node(4))
insert(bst2.root, Node(11))
insert(bst2.root, Node(16))
insert(bst2.root, Node(21))
insert(bst2.root, Node(24))
insert(bst2.root, Node(23))
insert(bst2.root, Node(27))
insert(bst2.root, Node(25))
insert(bst2.root, Node(26))

print bst2.root.value

print
print bst2.root.left.value
print bst2.root.left.left.value
print bst2.root.left.left.left.value
print bst2.root.left.left.right.value
print bst2.root.left.right.value
print bst2.root.left.right.right.value
print bst2.root.left.right.right.value
print bst2.root.left.right.right.value

print
print bst2.root.right.value
print bst2.root.right.right.value
print bst2.root.right.right.left.value
print bst2.root.right.right.right.value
print bst2.root.right.right.right.left.value
print bst2.root.right.right.right.left.right.value

print super_balanced(bst2.root)
