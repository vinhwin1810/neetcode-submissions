class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def dfs(i, end, memo):
            if i > end:
                return 0
            if i in memo:
                return memo[i]
            first_choice = dfs(i+1, end, memo)
            second_choice = nums[i] + dfs(i+2, end, memo)

            memo[i] = max(first_choice, second_choice)

            return memo[i]
        
        return max(dfs(0, len(nums) - 2, {}), dfs(1, len(nums) - 1, {}))
            