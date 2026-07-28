class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights),sum(weights)
        minweight = float('inf')
        while l<=r:
            mid = (l+r)//2
            if self.possible(weights,mid,days):
                minweight = min(minweight,mid)
                r = mid-1
            else:
                l=mid+1
        return minweight



    def possible(self,weights,capacity,days):
        cap=0
        day=0
        for i in range(len(weights)):
            cap+=weights[i]
            if cap==capacity:
                cap=0
                day+=1
            elif cap>capacity:
                cap=weights[i]
                day+=1
        if cap>0:
            day+=1
        if day>days:
            return False
        return True


        