class BST():
    def __init__(self, root):
        self.root = root

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, node):
    if root == None:
        root = node
    elif node.value < root.value:
        if root.left == None:
            root.left = node
        else:
            insert(root.left, node)
    elif node.value > root.value:
        if root.right == None:
            root.right = node
        else:
            insert(root.right, node)

# So to find the heaviest weighted path from root to leaf-

# Use recursive dfs- passing along the weight of the path as you go
# i.e. as you visit a node- recurse on the children it has and add the value
# of the node

# if we arrive at a node that doesn't have a left or right child- we're at a leaf
# and we add this distance to an array of leaf_distances

# we then take the max of this array
def heaviest_weighted_path(root):
    leaf_distances = []
    heaviest_helper(root, 0, leaf_distances)
    print leaf_distances
    return max(leaf_distances)

def heaviest_helper(root, dist_so_far, leaf_distances):
    # Want a return here because we don't want to consider the following
    # if statements if we enter this case
    if not root.left and not root.right:
        leaf_distances.append(dist_so_far + root.value)
        return
    # Don't want a return here otherwise we could skip a case
    if root.left:
        heaviest_helper(root.left, dist_so_far + root.value, leaf_distances)
    if root.right:
        heaviest_helper(root.right, dist_so_far + root.value, leaf_distances)

def inorder(root):
    if root != None:
        inorder(root.left)
        print root.value
        inorder(root.right)

def preorder(root):
    if root != None:
        print root.value
        inorder(root.left)
        inorder(root.right)

bst = BST(Node(5))
insert(bst.root, Node(1))
insert(bst.root, Node(2))
insert(bst.root, Node(3))
insert(bst.root, Node(4))
#
# inorder(bst.root)
# print
# preorder(bst.root)

print
print bst.root.left.value
print bst.root.left.right.value
print bst.root.left.right.right.value
print bst.root.left.right.right.right.value
print

print heaviest_weighted_path(bst.root)

bst2 = BST(Node(2))
insert(bst2.root, Node(1))
insert(bst2.root, Node(3))

print heaviest_weighted_path(bst2.root)

bst3 = BST(Node(8))
insert(bst3.root, Node(3))
insert(bst3.root, Node(10))
insert(bst3.root, Node(1))
insert(bst3.root, Node(6))
insert(bst3.root, Node(14))
insert(bst3.root, Node(4))
insert(bst3.root, Node(7))
insert(bst3.root, Node(13))
print heaviest_weighted_path(bst3.root)

# Find the heaviest weight path from root to leaf
# Return the weight itself and not the path

# Heaviest path: greatest sum of node data from root to leaf

     #    2
     #  /   \
     # 1     3
