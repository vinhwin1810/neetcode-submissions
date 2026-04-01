class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        max_len = 0
        cur_char = set()
        
        for r in range(n):
            while s[r] in cur_char:
                cur_char.remove(s[l])
                l += 1
            
            cur_char.add(s[r])
            max_len = max(max_len, r - l + 1)  # Update max length after adding

        return max_len