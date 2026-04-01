class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        candidates.sort()
        self.prev = -1
        def backtrack(start, sub, target):
            if target == 0:
                res.append(sub.copy())
                return 
            # prev = -1
            for i in range(start, len(candidates)):
                if candidates[i] > target or candidates[i] == self.prev:
                    continue
                
                sub.append(candidates[i])
                backtrack(i+1, sub, target - candidates[i])
                sub.pop()
                self.prev = candidates[i]


        backtrack(0, [], target)
        return res