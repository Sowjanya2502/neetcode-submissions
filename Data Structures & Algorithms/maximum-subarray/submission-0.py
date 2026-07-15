class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        final = nums[0]
        for i in range(1,len(nums)):
            result +=nums[i]
            if result<nums[i]:
                result = nums[i]
            final=max(final,result)
        return final

        