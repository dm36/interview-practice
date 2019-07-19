# BST to have a concept of a root
# https://github.com/OmkarPathak/Data-Structures-using-Python/blob/master/Trees/BinarySearchTree.py
class BST():
  def __init__(self, root):
    self.root = root

# Node to have a concept of a value and a left and right subtree
class Node():
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def insert(root, node):
  if root == None:
    root = Node
  else:
    # insert to the left
    if node.value < root.value:
      if root.left == None:
        root.left = node
      else:
        return insert(root.left, node)
    # think else if get's evaluated after the above
    # return while else doesn't??
    # else if node.value > root.right:
    else:
      if root.right == None:
        root.right = node
      else:
        return insert(root.right, node)

def inorder(root):
    if root != None:
        inorder(root.left)
        print (root.value)
        inorder(root.right)

bst = BST(Node(5))
insert(bst.root, Node(1))
insert(bst.root, Node(2))
insert(bst.root, Node(3))
insert(bst.root, Node(4))
insert(bst.root, Node(6))
insert(bst.root, Node(7))
insert(bst.root, Node(8))

inorder(bst.root)
