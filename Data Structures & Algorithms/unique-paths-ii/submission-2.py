class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = [[-1]*(len(obstacleGrid[0])) for i in range(len(obstacleGrid))]

        def dfs(obstacleGrid, r, c):
            if r>=len(obstacleGrid) or c>=len(obstacleGrid[0]) or obstacleGrid[r][c]==1:
                return 0
            if r == len(obstacleGrid)-1 and c == len(obstacleGrid[0])-1:
                return 1
            if memo[r][c]!=-1:
                return memo[r][c] 
            memo[r][c]=dfs(obstacleGrid,r,c+1)+dfs(obstacleGrid,r+1,c)

            return memo[r][c]

        return dfs(obstacleGrid,0,0)