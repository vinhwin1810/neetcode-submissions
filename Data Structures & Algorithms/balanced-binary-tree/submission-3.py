# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [0, True]  # Base case: empty node is balanced with height 0
            
            # Get the height and balance status for the left and right subtrees
            l, left_balanced = dfs(node.left)
            r, right_balanced = dfs(node.right)
            
            # Check if the current node is balanced
            if abs(l - r) > 1 or not left_balanced or not right_balanced:
                return [0, False]  # If unbalanced, return height 0 and False
            
            # Return the height of the current node and whether it's balanced
            return [max(l, r) + 1, True]
        
        # The tree is balanced if the second value is True
        return dfs(root)[1]

        



