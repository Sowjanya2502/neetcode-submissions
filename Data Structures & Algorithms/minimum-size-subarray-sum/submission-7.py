class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r = 0,0
        sum1, result = 0, float('inf')
        while r <len(nums):
            sum1 += nums[r]
            while sum1 >= target:
                result =  min(result, r-l+1)
                sum1 -= nums[l]
                l+=1
            r+=1 
        return result if result != float('inf') else 0
        