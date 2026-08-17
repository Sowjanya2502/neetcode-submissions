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
            for _ in range(len(queue)):
                row,column = queue.popleft()
                dir=[(-1,0),(1,0),(0,1),(0,-1)]
                for di in dir:
                    nextr,nextc = row+di[0], column+di[1]
                    if self.withinbounds(grid,nextr,nextc) and grid[nextr][nextc]==1:
                        grid[nextr][nextc]=2
                        count-=1
                        queue.append((nextr,nextc))
        return time if count==0 else -1




    def withinbounds(self,grid, row, column):
        return 0<=row<len(grid) and 0<=column<len(grid[0])
            

        