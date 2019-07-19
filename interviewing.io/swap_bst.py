# https://www.geeksforgeeks.org/fix-two-swapped-nodes-of-bst/

class BST():
    def __init__(self, root):
        self.root = root

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# compare node to root- if node is < than root and root
# doesn't have a left child, make the node the left child
# otherwise recurse on the left subtree- inserting there

# same idea with the right subtree
def insert(root, node):
    if root == None:
        root = node

    if node.value < root.value:
        if root.left == None:
            root.left = node
        else:
            insert(root.left, node)

    elif node.value > root.value:
        if root.right == None:
            root.right = node
        else:
            insert(root.right, node)

def swap_bst(root):
    return swap_bst_helper(root, None, Node(float("-inf")), Node(float("inf")))

def swap_bst_helper(node, parent, lower, upper):
    # doesn't make sense for us to follow any of the future steps
    # if the node is None
    if not node:
        return


    if parent:
        # swap the node with its parent if the node is a left
        # child with a value greater than its parent
        if node.value > parent.value and node == parent.left:
            temp_value = node.value
            node.value = parent.value
            parent.value = temp_value
            return

        # swap the node with its parent if the node is a right
        # child with a value less than its parent
        if node.value < parent.value and node == parent.right:
            temp_value = node.value
            node.value = parent.value
            parent.value = temp_value
            return

    # swap with the node imposing the lower obund if the node's value
    # is less than the lower bound
    if node.value < lower.value:
        temp_value = node.value
        node.value = lower.value
        lower.value = temp_value
        return

    # swap with the node imposing the upper bound if the node's value
    # is greater than the upper bound
    if node.value > upper.value:
        temp_value = node.value
        node.value = upper.value
        upper.value = temp_value
        return

    return swap_bst_helper(node.left, node, lower, node)
    return swap_bst_helper(node.right, node, node, upper)

def is_valid(root):
    return is_valid_helper(root, -float("inf"), float("inf"))

def is_valid_helper(root, lower_bound, upper_bound):
    if not root:
        return True

    # if the root is less than the lower bound or greater than the upper bound
    # return False
    if root.value < lower_bound or root.value > upper_bound:
        return False

    # recursively impose bounds on left and right subtrees-
    # left subtree is upper bounded by the root's value and the right
    # subtree is lower bounded by the root's value
    return is_valid_helper(root.left, lower_bound, root.value) and is_valid_helper(root.right, root.value, upper_bound)


root = Node(5)
insert(root, Node(3))
insert(root, Node(4))
insert(root, Node(6))
insert(root, Node(7))

print is_valid(root)

root2 = Node(1)
root2.left = Node(3)
root2.left.right = Node(2)

print is_valid(root2)
print root2.value
print root2.left.value
print root2.left.right.value

swap_bst(root2)
print root2.value
print root2.left.value
print root2.left.right.value
