class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        total = sum(nums)
        l, r = max(nums), total
        res = 0
        while l<=r:
            m = (l+r)//2
            if self.splitintok(nums,k,m):
                res = m
                r = m-1
            else:
                l = m+1
        return res
    def splitintok(self, nums, k,m):
        cur_sum = 0
        for num in nums:
            cur_sum = cur_sum+num
            if cur_sum>m:
                k=k-1
                if k<1:
                    return False
                cur_sum = num
        return True





        