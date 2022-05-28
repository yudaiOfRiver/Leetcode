class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        print(m, n)
        paths = [[0]*n for i in range(m)]

        for c in range(n-1, -1, -1):     # initial set about last Row
            if obstacleGrid[-1][c] == 1: break
            paths[-1][c] = 1

        for r in range(m-1, -1, -1):
            print(r)
            if obstacleGrid[r][-1] == 1: break
            paths[r][-1] = 1

        for c in range(n-2,-1, -1):
            for r in range(m-2, -1, -1):
                if obstacleGrid[r][c] == 1: continue
                paths[r][c] = paths[r+1][c] + paths[r][c+1]

        return(paths[0][0])


