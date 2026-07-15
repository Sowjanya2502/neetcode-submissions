class Solution:
    def numDecodings(self, s: str) -> int:
        # n=len(s)
        # dp=[0]*(n+1)
        # dp[n]=1
        # for i in range(len(s)-1,-1,-1):
        #     if s[i]=='0':
        #         dp[i]=0
        #     else:
        #         dp[i]=dp[i+1]
        #     if ((i+1<len(s)) and (s[i]=='1' or s[i]=='2' and s[i+1] in '0123456')):
        #         dp[i]+=dp[i+2]
        # return dp[0]
        memo={len(s):1}
        # res=0
        def dfs(i):
            if i in memo:
                return memo[i]
            if s[i]=='0':
                return 0
            res=dfs(i+1)
            if (i+1<len(s)) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                res += dfs(i+2)
            memo[i]=res
            return res
        return dfs(0)
            






            



            
        