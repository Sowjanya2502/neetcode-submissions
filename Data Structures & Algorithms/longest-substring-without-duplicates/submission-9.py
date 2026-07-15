class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = set()
        l=0
        length = 0
        for i in range(0, len(s)):
            while s[i] in res:
                res.remove(s[l])
                l+=1
            res.add(s[i])
            length = max(length, i-l+1)
        return length
