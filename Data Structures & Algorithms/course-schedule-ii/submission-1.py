class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree=[0]*numCourses
        dictmap = defaultdict(list)
        for pre in prerequisites:
            indegree[pre[0]]+=1
            dictmap[pre[1]].append(pre[0])
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        res = []
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                res.append(node)
                for pre in dictmap[node]:
                    indegree[pre]-=1
                    if indegree[pre]==0:
                        queue.append(pre)
        return res if len(res)==numCourses else []

