class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = []
        s=0
        for i in range(0, len(prices)-1):
            res.append(prices[i+1]- prices[i])
        for r in res:
            if r >=0:
                s = s+r
        return s