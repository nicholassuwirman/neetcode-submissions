# two pointers
# res = 0

#                          l r
# Input: height = [1,7,2,5,4,7,3,6]
# calcu = (r - l) * (min(heights[l], heights[r]))
# 1. calcu = 7 * 1 = 7
# 2. calcu = 6 * 6 = 36
# 3. calcu = 5 * 3 = 15
# 4. calcu = 4 * 7 = 28
# 5. calcu = 3 * 2 = 6
# 6. calcu = 2 * 2 = 4
# 7. calcu = 1 * 3 = 3


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights)-1
        while l < r:
            calcu = (r - l) * (min(heights[l], heights[r]))
            if calcu > res:
                res = calcu
            if heights[l] <= heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
        return res