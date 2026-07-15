class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        maxweight = sum(weights)
        if days==1:
            return maxweight
        left,right = max(weights), sum(weights)
        least = sum(weights)
        while left <= right:
            mid = (left + right)//2
            if self.weightpossible(mid,weights,days):
                least = min(least, mid)
                right = mid-1
            else:
                left = mid+1
        return least

    def weightpossible(self,minweight, weights, days):
        ndays,curr_weight = 1,minweight
        for w in weights:
            if curr_weight-w<0:
                ndays+=1
                curr_weight = minweight
                if ndays>days:
                    return False
            curr_weight = curr_weight-w
        return True

                
            
