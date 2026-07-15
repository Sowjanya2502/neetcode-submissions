class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for item in stones:
            heapq.heappush(max_heap, -item)
        while len(max_heap)>1:
            first = abs(heapq.heappop(max_heap))
            if abs(max_heap[0])==(first):
                heapq.heappop(max_heap)
            elif first > abs(max_heap[0]):
                second=abs(heapq.heappop(max_heap))
                heapq.heappush(max_heap, -(abs(second - first)))
        return abs(max_heap[0]) if len(max_heap)>0 else 0        