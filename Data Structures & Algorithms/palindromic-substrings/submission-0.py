class Solution:
    def countSubstrings(self, s: str) -> int:
        # even
        res = 0
        for i in range(len(s)):
            l, r = i, i
            while l > -1 and r < len(s):
                if s[l] != s[r]:
                    break
                else:
                    res += 1
                    l -=1
                    r += 1
        # odd
        for i in range(len(s)):
            l, r = i, i+1
            while l > -1 and r < len(s):
                if s[l] != s[r]:
                    break
                else:
                    res += 1
                    l -=1
                    r += 1
        return res
