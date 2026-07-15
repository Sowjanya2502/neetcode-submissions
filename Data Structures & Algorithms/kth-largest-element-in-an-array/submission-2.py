class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap=[]
        count = 0
        for i in range(len(nums)):
            heapq.heappush(minHeap, -nums[i])
        while count<k-1:
            heapq.heappop(minHeap)
            count+=1
        return -(heapq.heappop(minHeap))