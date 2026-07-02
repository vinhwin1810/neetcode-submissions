class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        ans = 0
        for i in nums:
            if i - 1 not in nums:
                streak = 0
                while i in nums:
                    i += 1
                    streak += 1
                ans = max(ans, streak)
        return ans
            