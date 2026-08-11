class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        map1=defaultdict(list)
        res=0
        for e in edges:
            map1[e[0]].append(e[1])
            map1[e[1]].append(e[0])
        visited = [False]*n
        def dfs(node):
            for nb in map1[node]:
                if not visited[nb]:
                    visited[nb]=True
                    dfs(nb)
        for i in range(n):
            if not visited[i]:
                visited[i]=True
                dfs(i)
                res+=1
        return res
