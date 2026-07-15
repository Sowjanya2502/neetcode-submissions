class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        result = right
        while left<=right:
            mid = (left+right)//2
            if self.meetsh(mid,piles,h):
                result = min(result,mid)
                right = mid-1
            else:
                left = mid+1
        return result
        


    def meetsh(self,mid,piles,h):
        nohours=0
        for p in piles:
            nohours+=math.ceil(float(p) / mid)
            if nohours>h:
                return False
        return True


