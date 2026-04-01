class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin, curMax = 1, 1
        res = -math.inf
        for num in nums:
            if num == 0:
                curMin = curMax = 1
                res = max(res, 0)
                continue
            
            tmp = curMin
            curMin = min(num, curMin * num, curMax * num)
            curMax = max(num, curMax * num, tmp * num)
            res = max(res, curMax)

        return res
            