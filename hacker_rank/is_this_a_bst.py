""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
arr = []

def checkValid(root, low, high):
    if root == None:
        return True
    arr.append(root.data)
    if root.data < low or root.data > high:
        return False
    else:
        return checkValid(root.left, low, root.data) and checkValid(root.right, root.data, high)

def checkDistinct(arr):
    arr.sort()
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            return False
    return True

def checkBST(root):
    valid = checkValid(root, -float("inf"), float("inf"))
    distinct = checkDistinct(arr)

    state = True if valid and distinct else False
    return state
