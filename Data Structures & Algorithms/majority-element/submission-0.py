class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map_result = defaultdict(int)
        for num in nums:
            map_result[num] += 1
        for key,value in map_result.items():
            if value > len(nums)/2:
                return key
