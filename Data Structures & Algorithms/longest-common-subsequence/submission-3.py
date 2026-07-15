class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def lcs(l1,l2):
            if l1==len(text1) or l2==len(text2):
                return 0
            if (l1,l2) in memo:
                return memo[(l1,l2)]
            if text1[l1]==text2[l2]:
                memo[(l1,l2)] = 1+lcs(l1+1,l2+1)
            else:
                 memo[(l1,l2)] = max(lcs(l1,l2+1), lcs(l1+1,l2))
            return memo[(l1,l2)]
        
        return lcs(0,0)

                


        