class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minHeap = []
        maxHeap=[]
        res = 0
        for i in range(len(capital)):
            heapq.heappush(minHeap,(capital[i],i))
        for i in range(k):
            while minHeap and minHeap[0][0]<=w:
                c, i = heapq.heappop(minHeap)
                heapq.heappush(maxHeap,-profits[i])
            if not maxHeap:
                break
            p = heapq.heappop(maxHeap)
            w = w - p
        return w