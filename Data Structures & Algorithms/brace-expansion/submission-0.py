class Solution:
    def expand(self, s: str) -> List[str]:
        ans = []
        def backtrack(i, sub):
            if i == len(s):
                ans.append(sub)
                return
            
            char = s[i]
            if char.isalpha():
                backtrack(i+1, sub + char)
            else:
                j = i
                options = []
                while s[j] != "}":
                    if s[j].isalpha():
                        options.append(s[j])
                    j += 1
                for option in options:
                    backtrack(j+1, sub + option)
        
        backtrack(0, "")
        return ans