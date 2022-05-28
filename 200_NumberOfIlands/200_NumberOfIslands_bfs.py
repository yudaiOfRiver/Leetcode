from collections import deque

class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        island = 0
        
        def bfs_in_island(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))
            while queue:
                row, col = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and
                       c in range(cols) and
                       (r,c) not in visited and
                       grid[r][c] == "1"):
                        queue.append((r, c))
                        visited.add((r, c))
                
                   
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                   bfs_in_island(r, c)
                   island += 1
                   print(visited)
        return island