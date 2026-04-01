class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        product = 1
        seen_zero = 0
        for num in nums:
            if num == 0:
                seen_zero += 1
                continue
            product *= num
        if seen_zero > 1:
            return [0] * len(nums)
        for num in nums:
            if seen_zero == 1:
                res.append(0) if num != 0 else res.append(product)
            else:
                res.append(product // num)
        return res