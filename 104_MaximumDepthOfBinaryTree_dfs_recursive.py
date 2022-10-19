#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        cur = root
        if cur is None:
            return 0

        return 1 + max(self.maxDepth(cur.left), self.maxDepth(cur.right))
