class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        mp={}
        minHeap=[]
        res=[]
        for i in range(len(points)):
            p=points[i]
            mp[i]=math.sqrt(p[0] ** 2 + p[1] ** 2 )
        for key,value in mp.items():
            heapq.heappush(minHeap,(value,key))
        while len(res)<k:
            max_distance1 = heapq.heappop(minHeap)
            res.append(points[max_distance1[1]])
        return res