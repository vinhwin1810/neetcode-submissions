class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = Counter(s1)
        count2 = {}
        l = 0
        for r in range(len(s2)):
            count2[s2[r]] = count2.get(s2[r], 0) + 1

            if r - l + 1 == len(s1):
                if count2 == count1:
                    return True
                count2[s2[l]] -= 1
                if count2[s2[l]] == 0:
                    del count2[s2[l]]
                l += 1
        return False