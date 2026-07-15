class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count =0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    count+=self.dfs(grid, i, j)
        return count
    def dfs(self,grid, row, column):
        grid[row][column]="-1"
        index = [(0,-1),(-1,0),(0,1),(1,0)]
        for d in index:
            r, c = row+d[0], column+d[1]
            if (self.withinbounds(grid,r,c) and grid[r][c]=="1"):
                self.dfs(grid,r,c)
        return 1        
        
    
    def withinbounds(self,grid, row, column):
        return 0<=row<len(grid) and 0<=column<len(grid[0])


        