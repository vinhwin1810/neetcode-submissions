class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # [2,-3,4,-2,2,1,-1,4]
        # [2, -1, 3, 1, 3, 4, 3, 7]
        # prefix sum
        # subarray[l:r] = prefix[r] - prefix[l-1]
        return self.divide_and_conquer(nums)
    def divide_and_conquer(self, nums):
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums)
        mid = (l + r) >> 1
        left_sum = self.divide_and_conquer(nums[:mid])
        right_sum = self.divide_and_conquer(nums[mid:])

        left = right = -math.inf
        cur = 0
        for i in range(mid - 1, -1, -1):
            cur += nums[i]
            left = max(left, cur)
        cur = 0
        for i in range(mid, len(nums)):
            cur += nums[i]
            right = max(right, cur)
        return max(left_sum, right_sum, left + right)

    def kadane(self, nums):
        ans = -math.inf
        min_prefix = 0
        prefix = 0
        for num in nums:
            prefix += num
            ans = max(ans, prefix - min_prefix)
            min_prefix = min(prefix, min_prefix)
        return ans


