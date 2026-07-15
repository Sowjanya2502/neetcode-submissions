class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        repeat=set()
        l,r=0,0
        max_length = 0
        while r<len(s):
            if s[r] in repeat:
                while s[r] in repeat:
                    repeat.remove(s[l])
                    l+=1
            repeat.add(s[r])
            max_length = max(max_length, r-l+1)
            r+=1
        return max_length