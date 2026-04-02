class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = ["" for _ in range(numRows)]
        cur_row = 0
        direction = 1
        for c in s:
            rows[cur_row] += c
            if cur_row == numRows - 1:
                direction = -1
            elif cur_row == 0:
                direction = 1
            cur_row += direction
        print(rows)
        return "".join(rows)