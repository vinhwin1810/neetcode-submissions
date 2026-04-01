from functools import cache

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        @cache
        def dfs(i):
            if i == len(s):
                return 0
            extra = 1 + dfs(i + 1)
            for word in dictionary:
                if s[i:i + len(word)] == word:
                    extra = min(extra, dfs(i+ len(word)))
            
            return extra
        return dfs(0)
                