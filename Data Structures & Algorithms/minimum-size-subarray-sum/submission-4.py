class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        presum = 0
        l = 0
        act_length = float('inf')
            
        for i in range(len(nums)):
            presum = presum + nums[i]
            nums[i] = presum
            if nums[i]>=target:
                act_length = min(act_length, i+1)
            while nums[i] - nums[l]>=target:
                act_length = min(act_length, i-l)
                l+=1
        if act_length!= float('inf'):
            return act_length
        else:
            return 0

