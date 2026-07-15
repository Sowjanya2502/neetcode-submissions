class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        max_result = 0
        while r<len(prices):
            if prices[r]-prices[l]>0:
                max_result = max(max_result, prices[r]-prices[l])
            else:
                l=r
            r+=1
        return max_result
            
            

       
