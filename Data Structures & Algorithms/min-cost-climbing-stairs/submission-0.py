class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        def dfs(i):
            if i >= len(cost):
                return 0
            min_choice = min(dfs(i+1), dfs(i+2))
            if i in dp:
                return dp[i]
            dp[i] = cost[i] + min_choice
            return dp[i]

        return min(dfs(0), dfs(1))