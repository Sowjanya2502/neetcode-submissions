class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map1=defaultdict(int)
        maxfreq=0
        l,r=0,0
        result = 0
        while r<len(s):
            map1[s[r]]+=1
            maxfreq = max(maxfreq, map1[s[r]])
            while ((r-l+1)-maxfreq)>k:
                map1[s[l]]-=1
                l+=1
            result = max(result, (r-l+1))
            r+=1
        return result
