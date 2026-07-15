class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_result = defaultdict(int)
        result=[]
        count = [[] for i in range(len(nums)+1)]
        for num in nums:
            map_result[num]+=1
        for key,value in map_result.items():
            count[value].append(key)
        for i in range(len(nums),0,-1):
            for j in count[i]:
                result.append(j)
                if len(result)==k:
                    return result
