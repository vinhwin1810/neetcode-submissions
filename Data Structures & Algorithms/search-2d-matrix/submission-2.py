class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # convert to array
        # 11: (1, 1)
        ROWS, COLS = len(matrix), len(matrix[0])
        # binary search
        low, high = 0, ROWS * COLS - 1
        while low <= high:
            mid = (low + high) // 2
            r, c = mid // COLS, mid % COLS
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False