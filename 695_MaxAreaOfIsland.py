class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0])
        visited = set()

        def dfs_in_island(i, j):      # calculate area of an island
            if (i in range(rows) and
               j in range(cols) and
               (i, j) not in visited and
               grid[i][j] == 1):
                visited.add((i, j))
                return 1 + dfs_in_island(i+1, j) \
                         + dfs_in_island(i-1, j) \
                         + dfs_in_island(i, j+1) \
                         + dfs_in_island(i, j-1)
            else:
                return 0

        area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    area = max(area, dfs_in_island(i, j))
        return area
