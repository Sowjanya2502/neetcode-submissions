class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 0,x
        result = 0
        while l<=r:
            mid = (l+r)//2
            sq = mid*mid
            if x == sq:
                return mid
            elif x>sq:
                l=mid+1
                result = mid
            else:
                r=mid-1
        return result
            

