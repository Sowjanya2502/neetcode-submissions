class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp1=Counter(s1)
        for i in range(len(s2)-len(s1)+1):
            if s2[i] in mp1:
                r=0
                mp2 = defaultdict(int)
                while r<len(s1):
                    mp2[s2[i+r]]+=1
                    r+=1
                if mp1==mp2:
                    return True
        return False

                    
                

            
            
