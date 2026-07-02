class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        ans = 0
        for r in range(len(s)):
            while s[r] in seen:
                ans = max(ans, r - l)
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
        return ans


