#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        stack = [[root, 1]]   # [node, level]
        res = 0
        while stack:
            cur, depth = stack.pop()
            if cur:
                res = max(res, depth)
                stack.append([cur.left, depth+1])
                stack.append(((cur.right, depth+1)))
        return res