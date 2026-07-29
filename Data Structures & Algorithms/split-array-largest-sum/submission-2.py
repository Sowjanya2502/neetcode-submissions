class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l,r = max(nums),sum(nums)
        res = 0
        while l<=r:
            mid = (l+r)//2
            if self.split(nums,mid,k):
                res = mid
                r=mid-1
            else:
                l=mid+1
        return res
    def split(self,nums,mid,k):
        curr_sum=0
        for i in range(len(nums)):
            curr_sum+=nums[i]
            if curr_sum>mid:
                k-=1
                if k<=0:
                    return False
                curr_sum = nums[i]
        return True

        