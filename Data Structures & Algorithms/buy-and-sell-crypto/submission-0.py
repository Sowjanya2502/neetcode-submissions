class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        longest = 0;
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                longest = max(longest, prices[j]-prices[i])
        return longest
        