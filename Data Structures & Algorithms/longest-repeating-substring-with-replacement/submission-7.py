class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        mp = defaultdict(int)
        max_length = 0
        result = 0
        for i in range(len(s)):
            mp[s[i]]+=1
            max_length = max(max_length,mp[s[i]])
            while (i-l+1)-max_length>k:
                mp[s[l]]-=1
                l+=1
                maxf = max(mp.values())
            result = max(result, i-l+1)
        return result

                

        