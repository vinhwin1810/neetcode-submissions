# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # at a node, left and right sum and nodeval
        # return up max(left or right + node.val) + update global res
        # res = max(res, left + right + node.val, left, right) # if negative => handle
        res = -math.inf
        def dfs(node):
            nonlocal res

            if not node:
                return -math.inf
            
            left = dfs(node.left)
            right = dfs(node.right)

            res = max(res, left, right, max(0, left) + node.val + max(0, right))

            return max(left, right, 0) + node.val
        dfs(root)
        return res

