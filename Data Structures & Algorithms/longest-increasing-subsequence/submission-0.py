class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i == len(nums):
                return 0
            if i in memo:
                return memo[i]
            
            longest = 1
            for j in range(i, len(nums)):
                if nums[j] > nums[i]:
                    longest = max(longest, 1 + dfs(j))
            memo[i] = longest
            return longest
        
        ans = 0
        for i in range(len(nums)):
            ans = max(ans, dfs(i))
        return ans
                