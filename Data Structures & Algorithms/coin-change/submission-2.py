class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = self.coinsrequired(coins, amount, {})
        return -1 if res == float('inf') else res

    def coinsrequired(self,coins:List[int], amount:int, memo:defaultdict()):
        if amount == 0:
            return 0
        if amount in memo:
            return memo[amount]
        mincoins = float('inf')
        for coin in coins:
            if coin <= amount:
                mincoins =min(mincoins,1+self.coinsrequired(coins, amount-coin, memo))
        memo[amount]=mincoins
        return memo[amount]
                
        