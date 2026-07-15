class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        res=[]
        for u,v in prerequisites:
            adj[v].append(u)
        prereqmap={}
        def dfs(node):
            if node not in prereqmap:
                prereqmap[node]=set()
                for nei in adj[node]:
                    prereqmap[node]=prereqmap[node] | dfs(nei)
                prereqmap[node].add(node)
            return prereqmap[node]
        for n in range(numCourses):
            dfs(n)
        for u,v in queries:
            res.append(u in prereqmap[v])
        return res

        
