class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # [2, 5, 1, 3, 5]
        n = len(nums) - 1
        for num in nums:
            if num < 0:
                num *= -1
            if nums[num - 1] < 0:
                return num
            nums[num - 1] *= -1
        
