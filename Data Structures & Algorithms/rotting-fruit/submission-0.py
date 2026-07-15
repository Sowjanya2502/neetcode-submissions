class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append((i,j))
        dires = [(-1,0),(0,-1),(1,0),(0,1)]
        time =0
        while fresh>0 and q:
            for _ in range(len(q)):
                r,c = q.popleft()
                for d in dires:
                    next_r, next_c = r+d[0], c+d[1]
                    if (next_r in range(len(grid))
                        and next_c in range(len(grid[0]))
                        and grid[next_r][next_c] == 1
                    ):
                        grid[next_r][next_c]=2
                        q.append((next_r, next_c))
                        fresh-=1
            time+=1
        return time if fresh==0 else -1
                






        

        