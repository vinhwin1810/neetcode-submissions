class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s):
            return s == s[::-1]
        def sol(start, sub):
            if start == len(s):
                print("adding")
                ans.append(sub[:])
                return
            
            for i in range(start + 1, len(s) + 1):
                if is_palindrome(s[start:i]):
                    sub.append(s[start:i])
                    sol(i, sub)
                    sub.pop()
        ans = []
        sol(0, [])
        return ans