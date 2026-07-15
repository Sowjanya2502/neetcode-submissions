class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        minHeap1=[]
        minHeap2 = []
        index=[]
        queue = deque()
        for i,(enq,deq) in enumerate(tasks):
            heapq.heappush(minHeap1,(enq,deq, i))
        time = 0
        while minHeap1 or minHeap2:
            while minHeap1 and minHeap1[0][0] <= time:
                enqueueTime, processTime, i = heapq.heappop(minHeap1)
                heapq.heappush(minHeap2, (processTime, i))

            if not minHeap2:
                time = minHeap1[0][0]
                continue

            processTime, i = heapq.heappop(minHeap2)
            time += processTime
            index.append(i)

        return index
        
        
        
        
        