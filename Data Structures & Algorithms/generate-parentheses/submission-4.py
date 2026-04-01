class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack, res = [], []
        def backtrack(opeN, closeD):
            if opeN == closeD == n:
                res.append("".join(stack))
                return
            if opeN < n:
                stack.append("(")
                backtrack(opeN + 1, closeD)
                stack.pop()
            if closeD < opeN:
                stack.append(")")
                backtrack(opeN, closeD + 1)
                stack.pop()
        backtrack(0, 0)
        return res
