class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        visit = set()
        def backtrack(row, col, i):
            if i == len(word):
                return True
            
            if row not in range(ROWS) or col not in range(COLS) or board[row][col] != word[i] or (row, col) in visit:
                return False
            visit.add((row, col))
            direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            for dr, dc in direction:
                if backtrack(row+dr, col+dc, i+1):
                    return True
            visit.remove((row, col))
            return False

        for i in range(ROWS):
            for j in range(COLS):
                if backtrack(i, j, 0):
                    return True
        
        return False