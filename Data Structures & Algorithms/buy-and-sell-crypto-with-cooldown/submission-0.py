class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}
        def dfs(i,buy):
            if i>=len(prices):
                return 0
            if (i,buy) in memo:
                return memo[(i,buy)]
            if buy:
                profit=dfs(i+1,not buy)-prices[i]
                memo[(i,buy)]=max(profit,dfs(i+1,buy))
            else:
                sell_profit = dfs(i+2, not buy)+prices[i]
                memo[(i,buy)]=max(sell_profit, dfs(i+1,buy))
            return memo[(i,buy)]
        return dfs(0,True)            

