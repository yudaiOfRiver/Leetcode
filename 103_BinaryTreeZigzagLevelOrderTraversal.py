# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root

        queue = collections.deque([[root, 1]])
        res = []
        while queue:
            nodes = []
            for i in range(len(queue)):
                node, level = queue.popleft()
                if level % 2 == 1: 
                    nodes.append(node.val)
                else:
                    nodes.insert(0, node.val)
                if node.left: queue.append([node.left, level+1]) 
                if node.right: queue.append([node.right, level+1])
            res.append(nodes)
        return res
