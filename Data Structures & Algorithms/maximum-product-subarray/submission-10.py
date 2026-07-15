class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # n=len(nums)
        # res=nums[0]
        # currmax,currmin = nums[0],nums[0]
        # for i in range(1,n):
        #     currmax=max(currmax*nums[i],nums[i],currmin*nums[i])
        #     currmin=min(nums[i]*currmin,nums[i],nums[i]*currmax)
        #     res = max(res,currmax)
        # return res
        res = nums[0]
        curMin, curMax = 1, 1

        for num in nums:
            tmp = curMax * num
            curMax = max(num * curMax, num * curMin, num)
            curMin = min(tmp, num * curMin, num)
            res = max(res, curMax)
        return res
        