class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        dist = 0
        while q:
            length = len(q)
            dist += 1
            for _ in range(length):
                r,c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row in range(ROWS) and col in range(COLS) and grid[row][col] == 2147483647:
                        grid[row][col] = dist
                        q.append((row, col))


