#              l       r
# prices = [10,1,5,6,7,1]
# max_profit = 6

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l, r = 0, 1

        while r < len(prices): 
            # case of 10 > 1, why stay at 10 when we can buy at 1 the next day? so shift l, r
            if prices[l] >= prices[r]:   
                l = r
            current_profit = prices[r] - prices[l]
            if current_profit > max_profit:
                max_profit = current_profit
            r += 1
        
        return max_profit