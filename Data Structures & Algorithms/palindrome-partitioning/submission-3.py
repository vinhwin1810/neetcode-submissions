class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(t):
            return t == t[::-1]
        
        res = []

        def dfs(start, sub):
            if start == len(s):
                res.append(sub[:])
                return
            
            for i in range(start, len(s)):
                if is_palindrome(s[start:i+1]):
                    sub.append(s[start:i+1])
                    dfs(i + 1, sub)
                    sub.pop()

        dfs(0, [])
        return res