class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res =0
        m,n=len(grid),len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    self.dfs(i,j,grid)
                    res+=1
        return res

    def dfs(self,r,c,grid):
        # if (r < 0 or c < 0 or r >= len(grid) or
        #         c >= len(grid[0]) or grid[r][c] == "0"):
        grid[r][c]='-1'
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        for di in dirs:
            next_r,next_c = r+di[0],c+di[1]
            if (self.withinbounds(grid,next_r,next_c) and grid[next_r][next_c]=='1'):
                self.dfs(next_r,next_c,grid)

    
    def withinbounds(self,grid, row, column):
        return 0<=row<len(grid) and 0<=column<len(grid[0])
        