# [3,6,7,11]  h = 8
#  1 is min             max(piles)                  
#  l         m          r  
# [1,2,3,4,5,6,7,8,9,10,11]
# using m = 6, koko eats the pile in 6 hours, which is < 8 (the h)
# we could try searching on the left side for a smaller possible solution for this

# but if using the m, koko eats the pile > than the h
# then search on the right (which means koko eats more per hour)

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        smallest = 0
        while l <= r:
            m = (l + r) // 2

            eatTime = 0
            for bananas in piles:
                eatTime += math.ceil(bananas / m)
            
            if eatTime <= h:
                r = m - 1
                smallest = m
            else: 
                l = m + 1
        
        return smallest