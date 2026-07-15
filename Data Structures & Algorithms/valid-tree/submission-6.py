class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        if len(edges) > (n - 1):
            return False
        def dfs(no,ne):
            if no in visited:
                return False
            visited.add(no)
            for nei in adj[no]:
                if nei == ne:
                    continue
                if not dfs(nei,no):
                    return False
            return True
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()
        return dfs(0,-1) and len(visited)==n 


        