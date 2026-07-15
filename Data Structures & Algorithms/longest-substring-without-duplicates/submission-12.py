class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = {}
        l=0
        length = 0
        for i in range(0, len(s)):
            if s[i] in res:
                l = max(res[s[i]]+1,l)
            res[s[i]]=i
            length = max(length, i-l+1)        
        return length
