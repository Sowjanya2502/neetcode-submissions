class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        dp=[[False for i in range(len(s))]for i in range(len(s))]
        count=0
        for i in range(n):
            dp[i][i]=True
            count+=1
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=True
                count+=1

        for i in range(3,n+1):
            for j in range(n-i+1):
                k=j+i-1
                if s[k]==s[j] and dp[j+1][k-1]:
                    dp[j][k]=True
                    count+=1
        return count