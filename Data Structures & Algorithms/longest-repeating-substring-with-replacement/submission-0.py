class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # ABBCCCDDDD k = 3
        max_len = 0
        ans = 0
        l = 0
        hashMap = {}
        for r in range(len(s)):
            hashMap[s[r]] = hashMap.get(s[r], 0) + 1
            max_len = max(max_len, hashMap[s[r]])
            while max_len + k < r - l + 1:
                hashMap[s[l]] -= 1
                if hashMap[s[l]] == 0:
                    del hashMap[s[l]]
                l += 1
            ans = max(ans, r - l + 1)
        return ans
