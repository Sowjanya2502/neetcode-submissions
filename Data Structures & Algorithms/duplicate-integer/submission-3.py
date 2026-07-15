class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myself=set()
        for i in nums:
            if i in myself:
                return True
            myself.add(i)
        return False