class Solution:
    def numDecodings(self, s: str) -> int:
        def dfs(i, memo):
            if i > len(s):
                return 0
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            count = 0
            if i in memo:
                return memo[i]
            first = dfs(i+1, memo)
            count += first

            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                second = dfs(i+2, memo)
                count += second
            memo[i] = count
            return memo[i]
        
        return dfs(0, {})
            
