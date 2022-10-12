class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()

        def dfs(r, c):
            direction = [[1, 0], [0, -1], [-1, 0], [0, 1]]
            for dr, dc in direction:
                row, col = r + dr, c + dc
                if row in range(rows) and col in range(cols) \
                    and (row, col) not in seen and grid[row][col] == "1":
                    seen.add((row, col))
                    dfs(row, col)

        res = 0
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in seen and grid[r][c] == "1":
                    seen.add((r, c))
                    dfs(r, c)
                    res += 1

        return res



grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
obj = Solution()
print(obj.numIslands(grid))
# Output: 1

