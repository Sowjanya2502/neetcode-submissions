class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)-1
        for i in range(len(nums)):
            for j in range(i+1, min(len(nums), k+i+1) ):
                if nums[i]==nums[j] and abs(i-j)<=k:
                    return True        
        return False