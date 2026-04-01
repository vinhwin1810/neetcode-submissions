class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPalindrome(s):
            return s == s[::-1]
        
        res = []
        def backtrack(start, sub):
            if start >= len(s):
                res.append(sub.copy())
                return
            
            for i in range(start, len(s)):
                cur = s[start:i+1]
                if isPalindrome(cur):
                    sub.append(cur)
                    backtrack(i+1, sub)
                    sub.pop()
                
        backtrack(0, [])
        return res