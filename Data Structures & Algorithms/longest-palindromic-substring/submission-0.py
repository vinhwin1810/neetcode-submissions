class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(s):
            return s == s[::-1]

        res = ""
        for i in range(len(s)):
            cur_str = ""
            for j in range(i, len(s)):
                cur_str += s[j]

                if isPalindrome(cur_str):
                    if len(cur_str) > len(res):
                        res = cur_str
        
        return res
