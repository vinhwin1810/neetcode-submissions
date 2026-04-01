class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        # for each row => create a set() add number and check presence O(n)
        # for each col 
        # for each box => 
        # [0][0] [0][1] [0][2] 
        # [1][0] [1][1] [1][2]
        # [2][0] [2][1] [2][2]
        # [4][0] [4][1] [4][2] 
        # [5][0] [5][1] [5][2]
        # [6][0] [6][1] [6][2]
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])
        
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in seen:
                    return False
                seen.add(board[j][i])
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = square // 3 * 3 + i
                    col = square % 3 *3 + j
                    if board[row][col] == ".":
                        continue     
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True