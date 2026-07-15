class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            b = target - nums[i]
            for j in range(i+1,len(nums)):
                if b == nums[j] and i!=j:
                    return [i,j]