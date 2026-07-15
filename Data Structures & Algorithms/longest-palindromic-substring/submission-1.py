class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        dp=[[False for i in range(len(s)+1)]for i in range(len(s)+1)]
        index=0
        length=1
        for i in range(n):
            dp[i][i]=True
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=True
                length = 2
                index=i
        for i in range(3,n+1):
            for j in range(n-i+1):
                k=j+i-1
                if s[k]==s[j] and dp[j+1][k-1]:
                    dp[j][k]=True
                    index=j
                    length = i
        return s[index:index+length]
        