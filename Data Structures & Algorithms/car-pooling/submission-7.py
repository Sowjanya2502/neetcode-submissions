class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])
        minHeap = []
        curPass=0
        for trip in trips:
            while minHeap and minHeap[0][0]<=trip[1]:
                curPass -= heapq.heappop(minHeap)[1]
            curPass += trip[0]
            if curPass>capacity:
                return False
            heapq.heappush(minHeap,(trip[2],trip[0]))

        return True