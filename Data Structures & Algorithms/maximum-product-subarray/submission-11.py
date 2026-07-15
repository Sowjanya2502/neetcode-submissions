class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        res=nums[0]
        currmax,currmin = nums[0],nums[0]
        for i in range(1,n):
            tmp=currmax*nums[i]
            currmax=max(currmax*nums[i],nums[i],currmin*nums[i])
            currmin=min(nums[i]*currmin,nums[i],tmp)
            res = max(res,currmax)
        return res

        