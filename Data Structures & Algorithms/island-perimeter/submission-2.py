class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.perimeter = 0
        res=0
        for r in range(0, len(grid)):
            for c in range(0, len(grid[0])):
                if grid[r][c]==1:
                    return self.dfs(r,c, grid)
        return res
    def dfs(self,r,c, grid):

        grid[r][c]=-1
        dirs = [(0,-1),(-1,0),(1,0),(0,1)]
        for di in dirs:
            next_r, next_c = r+di[0], c+di[1]
            if not self.withinbounds(next_r, next_c, grid) or grid[next_r][next_c] == 0:
                self.perimeter += 1
            elif self.withinbounds(next_r, next_c, grid) and grid[next_r][next_c]==1:
                self.dfs(next_r, next_c, grid)
        return self.perimeter
    
    def withinbounds(self,r,c, grid):
        return 0<=r<len(grid) and 0<=c<len(grid[0])    