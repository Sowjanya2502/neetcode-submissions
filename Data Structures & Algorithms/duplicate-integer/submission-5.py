class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setdup = set(nums)
        if len(setdup) != len(nums):
            return True
        return False