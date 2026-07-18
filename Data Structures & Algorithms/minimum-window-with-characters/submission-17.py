class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t =="":
            return ""
        countT = Counter(t)
        countS = defaultdict(int)
        have, need = 0, len(countT)
        resLen = float('inf')
        res = [-1,-1]
        l=0
        for i in range(len(s)):
            countS[s[i]]+=1
            if s[i] in countT and countT[s[i]]==countS[s[i]]:
                have +=1
            while have == need:
                if i-l+1 < resLen:
                    resLen = i-l+1
                    res=[l,i]
                countS[s[l]]-=1

                if s[l] in countT and countS[s[l]]<countT[s[l]]:
                    have -=1
                l+=1
        l,i=res
        return s[l:i+1] if resLen!=float('inf') else ""
                




        