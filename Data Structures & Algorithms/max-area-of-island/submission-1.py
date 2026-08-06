class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0
        self.area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    self.area = 1
                    maxarea = max(maxarea, self.dfs(grid,i,j))
        return maxarea

    def dfs(self,grid,row,column):
        if not self.withinbounds(grid,row, column) or grid[row][column]==0:
            return
        grid[row][column]=-1
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        for di in dirs:
            nextr,nextc = row+di[0],column+di[1]
            if (self.withinbounds(grid,nextr,nextc) and grid[nextr][nextc]==1):
                self.area+=1
                self.dfs(grid,nextr,nextc)
        return self.area

    def withinbounds(self,grid, row, column):
        return 0<=row<len(grid) and 0<=column<len(grid[0])