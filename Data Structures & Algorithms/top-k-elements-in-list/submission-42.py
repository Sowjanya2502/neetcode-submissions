class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_result = defaultdict(int)
        result=[]
        count = [[] for i in range(0,len(nums)+1)]
        for num in nums:
            map_result[num]+=1
        for key,value in map_result.items():
            count[value].append(key)
        for i in range(len(nums),0,-1):
            result = result+count[i]
            if len(result)>=k:
                return result[0:k]
