class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []
        l = 0
        max_element = 0
        for i in range(0, len(nums)):
            heapq.heappush(heap,(-nums[i],i))
            if i >= k-1:
                while heap[0][1] <= i-k:
                    heapq.heappop(heap)
                res.append((heap[0][0])*-1)
        return res

