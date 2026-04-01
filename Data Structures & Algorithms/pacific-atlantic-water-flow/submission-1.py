class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(0,1), (1, 0), (-1, 0), (0, -1)]
        res = []

        def pacific(r, c, visit=None):
            if visit is None:
                visit = set()
            if r == 0 or c == 0:
                return True
            visit.add((r, c))
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if (row in range(ROWS) and col in range(COLS) and heights[row][col] <= heights[r][c] and (row,col) not in visit and pacific(row, col, visit)):
                    return True
            return False
        

        def atlantic(r, c, visit = None):
            if visit is None:
                visit = set()
            if r == ROWS -1  or c == COLS - 1:
                return True
            visit.add((r, c))
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if (row in range(ROWS) and col in range(COLS) and heights[row][col] <= heights[r][c] and (row,col) not in visit and atlantic(row, col, visit)):
                    return True
            return False
        for r in range(ROWS):
            for c in range(COLS):
                if pacific(r, c) and atlantic(r, c):
                    res.append([r,c])
        
        return res










