class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i in range(0,len(nums)):
            if nums[i]==count:
                return count
            else:
                count = nums[i]