# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = collections.deque([root])
        res = 0        
        while queue:
            for i in range(len(queue)):   # for loop in the same level (BFS)
                cur = queue.popleft()
                if cur.left:  queue.append(cur.left)
                if cur.right: queue.append(cur.right)
            res += 1                    # increment about level

        return res