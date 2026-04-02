# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.total = 0
        def dfs(node):
            if not node:
                return 

            dfs(node.right)
            node.val, self.total = node.val + self.total, self.total + node.val
            dfs(node.left)
        dfs(root)
        return root
