# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Queue:
    def __init__(self):
        self.queue = []
    def add(self, item):
        self.queue.append(item)
    def remove(self):
        return self.queue.pop(0)
    def peek(self):
        return self.queue[0]
    def isEmpty(self):
        return len(self.queue) == 0


class Solution(object):
    def levelOrder(self, root):
        if root == None:
            return []
        level_queue = Queue()
        level_queue.add((root, 0))
        dist_map = collections.defaultdict(list)

        while not level_queue.isEmpty():
            node = level_queue.remove()
            dist_map[node[1]].append(node[0].val)
            if node[0].left:
                level_queue.add((node[0].left, node[1] + 1))
            if node[0].right:
                level_queue.add((node[0].right, node[1] + 1))
        return dist_map.values()
