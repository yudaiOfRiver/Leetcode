class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, possible):
            possible.add((r, c))
            directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
            for dr, dc in directions:
                rr, cc = r + dr, c + dc
                if rr in range(ROWS) and cc in range(COLS) and (rr, cc) not in possible:
                    if heights[rr][cc] >= heights[r][c]:
                        dfs(rr, cc, possible)


        for row in range(ROWS):
            dfs(row, 0, pac)
            dfs(row, COLS-1, atl)

        for col in range(COLS):
            dfs(0, col, pac)
            dfs(ROWS-1, col, atl)

        canFlowSet = pac & atl
        res = []
        for r, c in canFlowSet:
            res.append([r, c])
        return res

heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
obj = Solution()
print(obj.pacificAtlantic(heights))
