class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setdup = set()
        for i in range(0,len(nums)):
            setdup.add(nums[i])
        if len(setdup) != len(nums):
            return True
        return False