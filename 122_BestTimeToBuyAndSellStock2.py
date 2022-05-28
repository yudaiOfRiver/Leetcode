class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                maxP += prices[i+1] - prices[i]
        return maxP