class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPalindrome(s):
            return s == s[::-1]
        
        res = []
        def backtrack(s, sub):
            if not s:
                res.append(sub[:])
                return
            
            for i in range(1, len(s) + 1):
                cur = s[:i]
                if isPalindrome(cur):
                    sub.append(cur)
                    backtrack(s[i:], sub)
                    sub.pop()
            
        backtrack(s,[])
        return res