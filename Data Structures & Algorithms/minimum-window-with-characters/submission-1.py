class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = Counter(t)
        need = len(countT)

        countS = {}
        l = 0
        have = 0
        res = ""
        minLen = math.inf
        for r in range(len(s)):
            countS[s[r]] = countS.get(s[r], 0) + 1
            if countS[s[r]] == countT[s[r]]:
                have += 1
            
            while have == need:
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    res = s[l:r+1]
                countS[s[l]] -= 1
                if countS[s[l]] < countT[s[l]]:
                    have -=1
                l += 1
        return res