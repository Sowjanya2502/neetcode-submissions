class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        count = 0
        self.area=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    self.area=1
                    count = max(count,self.dfs(r,c,grid))
        return count
    def dfs(self,r,c,grid):
        grid[r][c]=-1
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        for di in dirs:
            next_r, next_c = r+di[0], c+di[1]
            if (self.withinboundaries(next_r,next_c,grid) and grid[next_r][next_c]==1):
                self.area +=1
                self.dfs(next_r,next_c,grid)
        return self.area
    def withinboundaries(self,r,c,grid):
        return 0 <= r < len(grid) and 0 <= c < len(grid[0])
