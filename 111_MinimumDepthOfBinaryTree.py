# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = collections.deque([[root, 1]])  # [node, level]
        leaf = set()

        while queue:
            for i in range(len(queue)):
                cur, depth = queue.pop()
                if cur.left:  queue.append([cur.left, depth+1])
                if cur.right: queue.append([cur.right, depth+1])
                if not cur.left and not cur.right:
                    leaf.add(depth)
        return min(leaf)
