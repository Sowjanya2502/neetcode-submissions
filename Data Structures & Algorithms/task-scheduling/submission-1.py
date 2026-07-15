class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp=defaultdict(int)
        maxHeap = []
        queue = deque()
        time = 0
        for task in tasks:
            mp[task] += 1
        for value in mp.values():
            heapq.heappush(maxHeap, -value)
        while maxHeap or queue:
            if not maxHeap:
                time = queue[0][1]
            else:
                freq = heapq.heappop(maxHeap)
                time +=1
                if freq+1!=0:
                    queue.append((freq+1, time+n))
            if queue and queue[0][1]==time:
                heapq.heappush(maxHeap,queue.popleft()[0])
        return time    
            

