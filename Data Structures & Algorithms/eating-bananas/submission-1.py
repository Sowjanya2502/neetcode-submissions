class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_bananas = max(piles)
        l,r=1,max_bananas
        minhour = float('inf')
        while l<=r:
            mid = (l+r)//2
            if self.possible(piles,h,mid):
                minhour = min(minhour, mid)
                r=mid-1                
            else:
                l=mid+1
        return minhour


    def possible(self,piles,hrs,perhour):
        count = 0
        for i in range(len(piles)):
            count += math.ceil(float(piles[i]) / perhour)
        if count>hrs:
            return False
        return True

        