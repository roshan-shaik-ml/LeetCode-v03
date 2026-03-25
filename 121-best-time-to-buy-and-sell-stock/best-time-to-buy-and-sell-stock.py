class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy, sell = 0, 0
        profit = 0
        while sell < len(prices):

            transaction = prices[sell] - prices[buy]
            print(buy, sell, transaction)
            if prices[sell] > prices[buy] and transaction > profit:
                profit = transaction
            elif prices[sell] < prices[buy]:
                buy = sell
            sell += 1
        return profit

            