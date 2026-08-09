class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree=[0]*numCourses
        graph = defaultdict(list)
        enrolledcourses=0
        for pre in prerequisites:
            indegree[pre[0]]+=1
            graph[pre[1]].append(pre[0])
        que=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                que.append(i)
        while que:
            key = que.popleft()
            enrolledcourses+=1
            for neighbors in graph[key]:
                indegree[neighbors]-=1
                if indegree[neighbors]==0:
                    que.append(neighbors)
        return enrolledcourses==numCourses


            