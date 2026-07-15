class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        minHeap1=[]
        minHeap2=[]
        for i,task in enumerate(tasks):
            heapq.heappush(minHeap1,(task[0],task[1],i))
        time = 0
        res = []
        while minHeap1 or minHeap2:
            while minHeap1 and minHeap1[0][0]<=time:
                available,timetaking, index = heapq.heappop(minHeap1)
                heapq.heappush(minHeap2,(timetaking,index))
            if not minHeap2:
                time = minHeap1[0][0]
                continue
            processtime, index = heapq.heappop(minHeap2)
            time = time+processtime
            res.append(index)
        return res



        
        
        
        