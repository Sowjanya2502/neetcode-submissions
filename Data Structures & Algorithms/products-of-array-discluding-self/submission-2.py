class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul=[0]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                mul[i]=1
            else:
                mul[i]=mul[i-1]*nums[i-1]
        postfix=1
        for i in range(len(nums)-1, -1,-1):
            mul[i]=postfix * mul[i]
            postfix = postfix*nums[i]
        return mul;