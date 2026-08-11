class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj=defaultdict(list)
        def dfs(node,par):
            if visit[node]:
                return True
            visit[node]=True
            for nei in adj[node]:
                if nei==par:
                    continue
                if dfs(nei,node):
                    return True
            return False

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visit = [False] * (len(edges) + 1)

            if dfs(u, -1):
                return [u, v]
        return []