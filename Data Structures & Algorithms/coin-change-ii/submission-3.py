class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dfs(target, start):
            if (target, start) in memo:
                return memo[(target, start)]
            if target == 0:
                return 1
            if target < 0 or start == len(coins):
                return 0
            
            count = 0
            for i in range(start, len(coins)):
                count += dfs(target - coins[i], i)
            memo[(target, start)] = count
            return memo[(target, start)]
        
        return dfs(amount, 0)
