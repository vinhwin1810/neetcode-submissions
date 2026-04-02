class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curSum = 0

        def dfs(node):
            nonlocal curSum
            if not node:
                return

            stack = []
            curr = node
            while stack or curr:
                while curr:
                    stack.append(curr)
                    curr = curr.right
                
                curr = stack.pop()
                tmp = curr.val
                curr.val += curSum
                curSum += tmp
                
                curr = curr.left

        dfs(root)
        return root