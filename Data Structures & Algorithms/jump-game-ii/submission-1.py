class Solution:
    def jump(self, nums: List[int]) -> int:
        memo={}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(nums)-1:
                return 0
            res = float('inf')
            last = min(len(nums)-1, i+nums[i])
            for j in range(i+1, last+1):
                res = min(res,1+dfs(j))
            memo[i]=res
            return res
        return dfs(0)


        