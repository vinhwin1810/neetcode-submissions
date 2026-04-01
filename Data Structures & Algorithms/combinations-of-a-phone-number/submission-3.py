class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = []

        def backtrack(start, combo):
            if len(combo) == len(digits):
                res.append(combo[:])
                return
            for i in range(start, len(digits)):
                for j in phone[digits[i]]:
                    combo+=j
                    backtrack(i+1, combo)
                    combo = combo[:-1]
        
        if not len(digits):
            return res
        backtrack(0, "")
        return res
