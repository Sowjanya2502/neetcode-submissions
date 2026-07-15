class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        frequence = []
        result = []
        for key,value in freq.items():
            heapq.heappush(frequence,(-value,key))
        for i in range(k):
            result.append(heapq.heappop(frequence)[1])
        return result
        