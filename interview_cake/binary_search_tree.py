class BinaryTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

bst = BinaryTreeNode(5)
left = bst.insert_left(4)
right = bst.insert_right(6)
print left.value
print right.value

left_left = left.insert_left(3)
print left_left.value 
