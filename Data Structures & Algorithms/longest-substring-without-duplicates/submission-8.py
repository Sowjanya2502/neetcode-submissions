class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        i = 1
        longest = 0
        if len(s)==1:
            return 1
        while i<len(s):
            if s[i] in s[l:i]:
                l = s.index(s[i],l,i)+1
            longest = max(longest, len(s[l:i])+1)          
            i+=1         
        return longest

