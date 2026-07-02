class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        hashMap = {}
    
        for i in nums:
            if i - 1 not in nums:
                hashMap[i] = 1
            else:
                hashMap[i] = hashMap[i - 1] + 1
        return max(hashMap.values())
            