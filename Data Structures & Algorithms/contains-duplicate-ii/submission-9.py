class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        resultset = set()
        j = 0
        for i in range(0,len(nums)):
            if abs(j-i)>k:
                resultset.remove(nums[j])
                j+=1
            if nums[i] in resultset:
                return True
            resultset.add(nums[i])
        return False
