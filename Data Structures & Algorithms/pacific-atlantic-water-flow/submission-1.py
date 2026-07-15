class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        m, n = len(heights), len(heights[0])
        direcs = [(-1,0),(0,-1),(1,0),(0,1)]

        def dfs(r, c):
            nonlocal pacific, atlantic
            if r < 0 or c < 0:
                pacific = True
                return
            if r >= m or c >= n:
                atlantic = True
                return

            if (r, c) in visited:
                return
            visited.add((r, c))

            for dr, dc in direcs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    if heights[nr][nc] <= heights[r][c]:
                        dfs(nr, nc)
                else:
                    dfs(nr, nc)

                # if pacific and atlantic:
                #     return

        for i in range(m):
            for j in range(n):
                pacific = False
                atlantic = False
                visited = set()
                dfs(i, j)
                if pacific and atlantic:
                    res.append([i, j])

        return res
        
        


        
