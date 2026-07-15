class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = set()
        length = 0
        l=0
        for i in range(0,len(s)):
            while s[i] in result:
                result.remove(s[l])
                l+=1
            result.add(s[i])
            length = max(length, i-l+1)
        return length