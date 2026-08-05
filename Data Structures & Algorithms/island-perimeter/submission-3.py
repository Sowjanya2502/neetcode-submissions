class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.res = 0
        def iswithinboundary(r,c,grid):
            if 0<=r<len(grid) and 0<=c<len(grid[0]):
                return True
            else:
                return False
        def dfs(grid, row, column):
            grid[row][column]=-1           
            dirs = [(-1,0),(1,0),(0,1),(0,-1)]
            for di in dirs:
                r,c = row+di[0], column+di[1]
                
                if not iswithinboundary(r,c,grid) or grid[r][c]==0:
                    self.res+=1
                elif iswithinboundary(r,c,grid) and grid[r][c]==1:
                    dfs(grid,r,c)
            return self.res
        
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(grid,i,j)
        
            