class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        network = defaultdict(list)
        time = 0
        dist = [float('inf')]*n
        for u,v,t in times:
            network[u].append((v,t))
        def dfs(node,time):
            if time >= dist[node-1]:
                return
            dist[node-1]=time
            for ne in network[node]:
                dfs(ne[0],time+ne[1])
        dfs(k,0)
        res = max(dist)
        return res if res<float('inf') else -1
            
        
        