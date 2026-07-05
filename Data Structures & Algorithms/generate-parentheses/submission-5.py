class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(open_bracket, close_bracket, s):
            if open_bracket > n:
                return
            if close_bracket > open_bracket:
                return
            if open_bracket == close_bracket == n:
                res.append(s)
                return
            
            backtrack(open_bracket + 1, close_bracket, s + "(")
            backtrack(open_bracket, close_bracket + 1, s + ")")
        backtrack(0, 0, "")
        return res