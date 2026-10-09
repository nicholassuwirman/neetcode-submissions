#  l  r
# [10,1,5,6,7,1]
#     l r
# [10,1,5,6,7,1]
#     l   r
# [10,1,5,6,7,1]
#     l     r
# [10,1,5,6,7,1]
#     l       r
# [10,1,5,6,7,1]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        l = 0
        r = 1
        highestPrice = 0

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                currentHighest = prices[r] - prices[l]
                highestPrice = max(highestPrice, currentHighest)
                r += 1
        return highestPrice    
            
        