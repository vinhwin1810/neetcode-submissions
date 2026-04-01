class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        target = total_sum // 2
        memo = {}
        def dfs(i, total):
            if i == len(nums):
                return False
            if total == target:
                return True
            elif total > target:
                return False
            if (i, total) in memo:
                return memo[(i, total)]

            memo[(i, total)] = dfs(i + 1, total + nums[i]) or dfs(i + 1, total)
            return memo[(i, total)]
        
        return dfs(0, 0)
