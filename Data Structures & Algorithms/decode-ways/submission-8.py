class Solution:
    def numDecodings(self, s: str) -> int:
        # pick this + pick this and next
        memo = {}
        def dfs(i):
            if i == len(s):
                return 1
            if i in memo:
                return memo[i]
            ways = 0
            if 1 <= int(s[i]):
                ways = dfs(i + 1)
                if i + 1 < len(s) and int(s[i:i+2]) <= 26:
                    ways += dfs(i + 2)
            memo[i] = ways
            return ways
        
        return dfs(0)
            
