class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        res=[]
        visited=set()
        for i,eq in enumerate(equations):
            adj[eq[0]].append([eq[1],values[i]])
            adj[eq[1]].append([eq[0],1/values[i]])
        def dfs(source, target, visited):
            if source not in adj or target not in adj:
                return -1
            if source ==target:
                return 1
            for ni,weight in adj[source]:
                if ni not in visited:
                    visited.add(ni)
                    result = dfs(ni,target,visited)
                    if result!=-1:
                        return weight*result
            return -1
        for q in queries:
            res.append(dfs(q[0],q[1],set()))
        return res