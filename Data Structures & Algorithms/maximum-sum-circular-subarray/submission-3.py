class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_max=global_max = nums[0]
        curr_min=global_min = nums[0]
        total=nums[0]
        for i in range(1,len(nums)):
            curr_min = min(nums[i], curr_min+nums[i])
            curr_max = max(nums[i], curr_max+nums[i])
            total += nums[i]
            global_max = max(global_max, curr_max)
            global_min = min(global_min, curr_min)
        return max(global_max, total - global_min) if global_max>0 else global_max
        