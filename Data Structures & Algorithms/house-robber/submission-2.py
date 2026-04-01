class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            first_choice = dfs(i+1)
            second_choice = nums[i] + dfs(i+2)

            memo[i] = max(first_choice, second_choice)
            
            print(i, first_choice, second_choice)
            return memo[i]
        
        return dfs(0)