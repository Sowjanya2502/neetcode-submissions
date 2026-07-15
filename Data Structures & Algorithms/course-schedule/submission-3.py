class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegree = [0]*numCourses
        for u1,u2 in prerequisites:
            adj[u1].append(u2)
            indegree[u2]+=1
        queue = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        enrolled=0
        while queue:
            pre=queue.popleft()
            enrolled+=1
            for nei in adj[pre]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    queue.append(nei)
        return enrolled==numCourses


