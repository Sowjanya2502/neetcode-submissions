class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        prev=1
        prevalue = 1
        if len(nums)==0:
            return nums
        for i in range(len(nums)):
            res[i]=prev
            prev = prev * nums[i]
        for i in range(len(res)-2,-1,-1):
            prevalue = prevalue * nums[i+1]
            res[i]=res[i]*prevalue
        return res
        
