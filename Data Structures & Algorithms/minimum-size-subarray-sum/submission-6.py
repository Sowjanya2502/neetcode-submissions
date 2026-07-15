class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minsum = float('inf')
        l=0
        sums =0
        for r in range(len(nums)):
            sums+=nums[r]
            while sums>=target:
                minsum = min(minsum, r-l+1)
                sums-=nums[l]
                l+=1
            r+=1
        return minsum if minsum!=float('inf') else 0
