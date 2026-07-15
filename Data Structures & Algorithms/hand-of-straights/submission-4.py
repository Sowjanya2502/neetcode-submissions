class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        map1=defaultdict(int)
        for n in hand:
            map1[n]+=1
        for h in hand:
            prev = h
            while map1[prev-1]:
                prev-=1
            while prev <=h:
                while map1[prev]>0:
                    for i in range(prev, prev+groupSize):
                        if i not in map1:
                            return False
                        map1[i]-=1
                prev+=1
        return True

        

        