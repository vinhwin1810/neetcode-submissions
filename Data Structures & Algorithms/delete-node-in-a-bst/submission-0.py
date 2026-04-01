# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return None
            
            if key > node.val:
                node.right = dfs(node.right)
            elif key < node.val:
                node.left = dfs(node.left)
            else:
                if not node.left:
                    return node.right
                cur = node.left
                print(cur.val)
                while cur.right:
                    cur = cur.right
                node.val = cur.val
                node.left = self.deleteNode(node.left, node.val)
            return node
        return dfs(root)