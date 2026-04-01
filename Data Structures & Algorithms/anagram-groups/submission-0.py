class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for s in strs:
            arr = [0]*26
            for c in s:
                arr[ord(c) - ord("a")] += 1
            if tuple(arr) not in hashMap:
                hashMap[tuple(arr)] = []
            hashMap[tuple(arr)].append(s)
        res = []
        for val in hashMap.values():
            res.append(val)
        return res

        
