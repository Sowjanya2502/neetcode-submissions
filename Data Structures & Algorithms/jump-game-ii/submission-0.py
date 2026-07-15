class Solution:
    def jump(self, nums: List[int]) -> int:
        def dfs(i):
            res = float('inf')
            if i == len(nums)-1:
                return 0
            last = min(len(nums)-1, i+nums[i])
            for i in range(i+1, last+1):
                res = min(res,1+dfs(i))
            return res
        return dfs(0)


        