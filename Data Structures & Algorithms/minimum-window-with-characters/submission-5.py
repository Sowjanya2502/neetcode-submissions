class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        mp1 = defaultdict(int)
        mp2 = defaultdict(int)
        res = [-1,-1]
        for i in range(len(t)):
            mp1[t[i]]+=1
        l = 0
        t1 = len(mp1)
        s1 = 0
        res_length = float("infinity")
        for i in range(len(s)):
            mp2[s[i]]+=1
            if s[i] in mp1 and mp2[s[i]] == mp1[s[i]]:
                s1+=1
            while s1 == t1:
                if (i-l+1)< res_length:
                    res = [l, i]
                    res_length = i-l+1

                mp2[s[l]]-=1
                if s[l] in mp1 and mp2[s[l]] < mp1[s[l]]:
                    s1 -=1
                l+=1
        l,c = res
        return s[l:c+1] if res_length != float("infinity") else "" 


            
                         