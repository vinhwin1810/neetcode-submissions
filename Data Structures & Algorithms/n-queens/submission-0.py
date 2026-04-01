class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        COLS = set()
        pos_DIAGS = set()
        neg_DIAGS = set()

        res = []
        board = [["."] * n for _ in range(n)]

        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n): 
                if c not in COLS and (r + c) not in pos_DIAGS and (r-c) not in neg_DIAGS:
                    COLS.add(c)
                    pos_DIAGS.add(r + c)
                    neg_DIAGS.add(r - c)
                    board[r][c] = "Q"
                    dfs(r + 1)
                    COLS.remove(c)
                    pos_DIAGS.remove(r + c)
                    neg_DIAGS.remove(r - c)
                    board[r][c] = "."
        
        dfs(0)
        return res