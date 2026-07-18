class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        elements = []
        res = []
        for i in range(len(nums)):
            heapq.heappush(elements,(-nums[i],i))
            if i>=k-1:
                while elements[0][1]<=i-k:
                    heapq.heappop(elements)
                res.append(-elements[0][0])
        return res
                
        