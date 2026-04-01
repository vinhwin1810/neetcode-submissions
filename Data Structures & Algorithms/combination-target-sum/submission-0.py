class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #distinct integer
        #unique combo

        res = []

        def backtrack(sub, target, start):
            if target < 0:
                return 
            if target == 0:
                res.append(sub.copy())
                return
            for i in range(start, len(nums)):
                sub.append(nums[i])
                backtrack(sub, target - nums[i], i)
                sub.pop()
        
        backtrack([], target, 0)
        return res            
