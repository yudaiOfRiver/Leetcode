class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:

        def bfs(i, j):
            stack = []
            stack.append((i, j))
            visited.add((i, j))
            directions = [[1, 0], [0, -1], [-1, 0], [0, 1]]
            while stack:
                cur_i, cur_j = stack.pop(0)
                for di, dj in directions:
                    i, j = cur_i + di, cur_j + dj
                    if (i in range(rows)) and (j in range(cols)) and (i, j) not in visited:
                        if grid[i][j] == "1":
                            stack.append((i, j))
                            visited.add((i, j))


        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        res = 0
        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visited and grid[row][col] == "1":
                    res += 1
                    bfs(row, col)
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
