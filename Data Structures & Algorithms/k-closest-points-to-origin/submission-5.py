class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap=[]
        res=[]
        for i in range(len(points)):
            p=points[i]
            value = math.sqrt(p[0] ** 2 + p[1] ** 2 )
            heapq.heappush(minHeap,(value,i))
        
        while len(res)<k:
            value,index = heapq.heappop(minHeap)
            res.append(points[index])
        return res