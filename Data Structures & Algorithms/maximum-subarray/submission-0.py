class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # [2,-3,4,-2,2,1,-1,4]
        # [2, -1, 3, 1, 3, 4, 3, 7]
        # prefix sum
        # subarray[l:r] = prefix[r] - prefix[l-1]
        ans = -math.inf
        min_prefix = 0
        prefix = 0
        for num in nums:
            prefix += num
            ans = max(ans, prefix - min_prefix)
            min_prefix = min(prefix, min_prefix)
        return ans


