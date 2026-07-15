class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map1=defaultdict(int)
        r=0
        max_freq, max_length = 0, 0
        for i in range(len(s)):
            map1[s[i]]+=1
            max_freq = max(max_freq, map1[s[i]])
            while (i-r+1)-max_freq >k:
                map1[s[r]]-=1
                r+=1

            max_length = max(max_length, i-r+1)
        
        return max_length
            



        