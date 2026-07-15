class Solution:
    def longestPalindrome(self, s: str) -> str:

        max_res = float('-inf')
        substring = ''
        for i in range(len(s)):
            #odd length
            l,r=i,i
            while l>=0 and r<=len(s)-1 and s[l]==s[r]:
                if (r-l+1) > max_res:
                    max_res = r-l+1
                    substring = s[l:r+1]
                l-=1
                r+=1
            l1,r1 = i,i+1
            while l1>=0 and r1<=len(s)-1 and s[l1]==s[r1]:
                if (r1-l1+1) > max_res:
                    max_res = r1-l1+1
                    substring = s[l1:r1+1]
                l1-=1
                r1+=1
        return substring