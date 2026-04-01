class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        #mark O on border to T
        def dfs(r, c):
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if row in range(ROWS) and col in range(COLS) and board[row][col] == "O":
                    board[row][col] = "T"
                    dfs(row, col)
        
        for r in range(ROWS):
            if board[r][0] == "O":
                board[r][0] = "T"
                dfs(r, 0)
            if board[r][COLS-1] == "O":
                board[r][COLS-1] = "T"
                dfs(r, COLS-1)
        
        for c in range(COLS):
            if board[0][c] == "O":
                board[0][c] = "T"
                dfs(0, c)
            if board[ROWS-1][c] == "O":
                board[ROWS-1][c] = "T"
                dfs(ROWS-1, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "T":
                    board[r][c] = "O"
