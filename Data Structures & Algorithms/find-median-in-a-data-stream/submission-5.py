class MedianFinder:

    def __init__(self):
        self.minRightHeap=[]
        self.maxLeftHeap=[]

    def addNum(self, num: int) -> None:
        if not self.maxLeftHeap or num <= -self.maxLeftHeap[0]:
            heapq.heappush(self.maxLeftHeap, -num)
            if len(self.maxLeftHeap)> len(self.minRightHeap)+1:
                heapq.heappush(self.minRightHeap, -heapq.heappop(self.maxLeftHeap))
        else:
            heapq.heappush(self.minRightHeap,num)
            if len(self.minRightHeap) > len(self.maxLeftHeap):
                heapq.heappush(self.maxLeftHeap, -heapq.heappop(self.minRightHeap))

        
        

    def findMedian(self) -> float:
        if len(self.minRightHeap)==len(self.maxLeftHeap):
            return (self.minRightHeap[0] - self.maxLeftHeap[0])/2
        else:
            return -self.maxLeftHeap[0]
        
        