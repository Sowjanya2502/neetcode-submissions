class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        m, n = len(heights), len(heights[0])
        direcs = [(-1,0),(0,-1),(1,0),(0,1)]
        self.pacific = False
        self.atlantic = False
        self.visited = set()

        def dfs(r, c):
            if r < 0 or c < 0:
                self.pacific = True
                return
            if r >= m or c >= n:
                self.atlantic = True
                return

            if (r, c) in self.visited:
                return
            self.visited.add((r, c))

            for dr, dc in direcs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    if heights[nr][nc] <= heights[r][c]:
                        dfs(nr, nc)
                else:
                    dfs(nr, nc)

        for i in range(m):
            for j in range(n):
                self.pacific = False
                self.atlantic = False
                self.visited = set()
                dfs(i, j)
                if self.pacific and self.atlantic:
                    res.append([i, j])

        return res
