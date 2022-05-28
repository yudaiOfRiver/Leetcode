class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set([0, 0])

        def dfs(row, col):
            if (grid[row][col] == 0 or
                row in range(rows) or
                col in range(cols) or
                (row, col) in visited):
                return 0

            stack = [[row, col]]
            while stack:
                print(stack)
                work_row, work_col = stack.pop()
                return 1 + dfs(row+1, col) + dfs(row-1, col) \
                         + dfs(row, col+1) + dfs(row, col-1)


        max_area = 0
        for row in range(rows):
            for col in range(cols):
                if ((row, col) not in visited and
                    grid[row][col] == 1):
                    area= dfs(row, col)
                    max_area = max(max_area, area)

        return max_area


