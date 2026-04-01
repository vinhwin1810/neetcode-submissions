class Solution:
    def trap(self, height: List[int]) -> int:
        max_l, max_r = [0]*len(height), [0]*len(height)
        l , r = 0, 0
        for i in range(len(height)):
            max_l[i] = l
            l = max(l, height[i])
        for j in range(len(height)-1, -1, -1):
            max_r[j] = r
            r = max(r, height[j])
        
        water = 0
        for h in range(len(height)):
            cur = min(max_l[h], max_r[h]) - height[h]
            if cur > 0:
                water += cur
        
        return water




        