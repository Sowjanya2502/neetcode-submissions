class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapr = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in mapr:
                return[mapr[diff],i]
            mapr[n] = i
        