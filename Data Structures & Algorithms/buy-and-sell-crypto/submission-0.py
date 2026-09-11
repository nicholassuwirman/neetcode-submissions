class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        sell_price = 0
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            
            current_sell_price = prices[i] - min_price
            
            if current_sell_price > sell_price:
                sell_price = current_sell_price
        return sell_price
                