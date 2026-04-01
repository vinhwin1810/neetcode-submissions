class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(sub):
            if len(sub) == len(nums):
                res.append(sub[:])
                return
            
            for num in nums:
                if num not in sub:
                    sub.append(num)
                    backtrack(sub)
                    sub.pop()
            
        backtrack([])
        return res