class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [-1]*len(nums)

        def dfs(i):
            if memo[i]!=-1:
                return memo[i]
            inti = 1
            for j in range(i+1, len(nums)):
                if nums[i]<nums[j]:
                    inti=max(inti,1+dfs(j))
            memo[i]=inti
            return memo[i]
        return max(dfs(i) for i in range(len(nums)))



