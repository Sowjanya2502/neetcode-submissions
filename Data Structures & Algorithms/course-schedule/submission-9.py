class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        graph = defaultdict(list)
        for crs,pre in prerequisites:
            indegree[crs]+=1
            graph[pre].append(crs)
        queue = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        enrolledcourses = 0
        while queue:
            node = queue.popleft()
            enrolledcourses +=1
            for neigbors in graph[node]:
                indegree[neigbors]-=1
                if indegree[neigbors]==0:
                    queue.append(neigbors)
        return enrolledcourses == numCourses

        
        
