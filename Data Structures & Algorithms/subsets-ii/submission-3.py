class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the input to easily handle duplicates
        res = []

        def backtrack(start, sub):
            res.append(sub.copy())  # Add the current subset to the result list

            prev = float("inf")
            for i in range(start, len(nums)):
                # Skip duplicates: if the current element is the same as the previous one, skip it
                if nums[i] == prev:
                    continue
                sub.append(nums[i])  # Add the current element to the subset
                backtrack(i + 1, sub)  # Recursively generate subsets with the next elements
                sub.pop()  # Backtrack: remove the last element to explore other subsets
                prev = nums[i]

        backtrack(0, [])  # Start the backtracking with an empty subset
        return res