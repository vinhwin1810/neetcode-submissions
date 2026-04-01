from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(k):
            hours = 0
            for banana in piles:
                hours += ceil(banana / k)
            return hours <= h
        
        low, high = 1, max(piles)
        res = 0
        while low <= high:
            mid = (low + high) // 2
            if canFinish(mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1

        return res