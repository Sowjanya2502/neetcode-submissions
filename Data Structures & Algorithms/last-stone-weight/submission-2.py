class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap=[]
        for s in stones:
            heapq.heappush(maxHeap,-s)
        while len(maxHeap)>1:
            first = abs(heapq.heappop(maxHeap))
            if abs(maxHeap[0])-first==0:
                heapq.heappop(maxHeap)
            elif first!=abs(maxHeap[0]):
                second = abs(heapq.heappop(maxHeap))
                heapq.heappush(maxHeap, -(abs(second - first)))
        return abs(maxHeap[0]) if len(maxHeap)>0 else 0
