class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map1 = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in map1 and abs(i-map1[nums[i]])<=k:
                return True
            map1[nums[i]]=i
        return False