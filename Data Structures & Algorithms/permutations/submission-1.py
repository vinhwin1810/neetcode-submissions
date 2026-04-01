class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(sub):
            if len(sub) == len(nums):
                res.append(sub.copy())
                return
            for i in range(len(nums)):
                if nums[i] in sub:
                    continue
                sub.append(nums[i])
                backtrack(sub)
                sub.pop()
            
        backtrack([])
        return res