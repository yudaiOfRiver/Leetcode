# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def buildSubTree(subpre, subin):
            if len(subpre) == 0:
                return None
            if len(subpre) == 1:
                return TreeNode(val=subpre[0])
            root = TreeNode(val=subpre[0])
            root_ind = subin.index(root.val)   # get index in inOrder of root
            root.left = buildSubTree(subpre[1:root_ind+1], subin[:root_ind])
            root.right = buildSubTree(subpre[root_ind+1:], subin[root_ind+1:])
            return root
        
        return buildSubTree(preorder, inorder)