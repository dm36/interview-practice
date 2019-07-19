# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        arr = []
        pre(root, arr)
        print arr
        return two_sum(arr, k)

def pre(root, arr):
    if not root:
        return

    if root:
        arr.append(root.val)
        pre(root.left, arr)
        pre(root.right, arr)

def two_sum(arr, target):
    my_set = set()

    for num in arr:
        if target - num in my_set:
            return True
        else:
            my_set.add(num)

    print my_set


    return False
