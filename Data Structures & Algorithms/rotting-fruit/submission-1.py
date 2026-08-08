class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = [0,0]
        count=0
        time=0
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]== 1:
                    count+=1
                elif grid[i][j]==2:
                    queue.append((i,j))
        
        while queue and count:
            time+=1
            for i in range(len(queue)):
                row,column = queue.popleft()
                for di in [(-1,0),(1,0),(0,-1),(0,1)]:
                    newr,newc = row+di[0], column+di[1]
                    if self.withinbounds(grid,newr,newc) and grid[newr][newc]==1:
                        grid[newr][newc]=2
                        queue.append((newr,newc))
                        count-=1
        return time if count==0 else -1



    def withinbounds(self,grid, row, column):
        return 0<=row<len(grid) and 0<=column<len(grid[0])
            

        