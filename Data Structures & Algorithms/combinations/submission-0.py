class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(start, sub, total):
            if total == k:
                res.append(sub[:])
                return
            
            for num in range(start, n + 1):
                sub.append(num)
                backtrack(num + 1, sub, total + 1)
                sub.pop()
        backtrack(1, [], 0)
        return res