class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # freq of s1 => hashMap
        # window of len(s1)

        count1 = {}
        for char in s1:
            count1[char] = count1.get(char, 0) + 1
        l = 0
        need = 0
        count2 = {}
        for r in range(len(s2)):
            count2[s2[r]] = count2.get(s2[r], 0) + 1
            # add char to count2
            # if char in count1 and cout in count2 = count in count 1 
            if s2[r] in count1 and count2[s2[r]] == count1[s2[r]]:
                need += 1
            elif s2[r] in count1 and count2[s2[r]] == count1[s2[r]] + 1:
                need -= 1
            if r - l + 1 == len(s1):
                if need == len(count1):
                    return True
                count2[s2[l]] -=1
                if s2[l] in count1 and count2[s2[l]] == count1[s2[l]] - 1:
                    need -=1
                elif s2[l] in count1 and count2[s2[l]] == count1[s2[l]]:
                    need += 1
                l += 1
        return False

        