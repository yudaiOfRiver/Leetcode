class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        res = 0
        rotted = set()
        oranges_num = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    rotted.add((row, col))
                if grid[row][col] == 1 or grid[row][col] == 2:
                    oranges_num += 1

        def rotten(r, c):
            print(r, c)
            directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
            for dr, dc in directions:
                rr, cc = r + dr, c + dc
                if (rr in range(ROWS)) and (cc in range(COLS)):
                    if grid[rr][cc] == 1:
                        rotted.add((rr, cc))
                        grid[rr][cc] = 2

        res = 0
        while True:
            print(rotted)
            tmp_rotted = rotted.copy()
            for (r, c) in tmp_rotted:
                rotten(r, c)
            if len(tmp_rotted) == len(rotted):
                break
            res += 1

        if oranges_num == len(rotted):
            return res
        else:
            return -1
