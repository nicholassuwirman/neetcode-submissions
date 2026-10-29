# [10,1,5,6,7,1]
#  l  r   
# [10,1,5,6,7,1]
#     l r
# [10,1,5,6,7,1]
#     l       r


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        if len(prices) == 1:
            return max_profit

        l = 0
        r = 1

        while r < len(prices) :
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                max_profit = max(max_profit, prices[r] - prices[l])
                r += 1
        
        return max_profit