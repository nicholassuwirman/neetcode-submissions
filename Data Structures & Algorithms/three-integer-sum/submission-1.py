# BF use 3 loops
# nums = [-1,0,1,2,-1,-4]
#          a,b,b,b, b, c
#          a,b,b,b, c, c
# a + b + c = 0

# Optimal
# nums = [-3,-3,1,2,3,4]
# O(n log n) + O(n^2) = O(n^2)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        # first loop, i = 0, a = -3
        # nums = [-3,-3,1,2,3,4]
        for i, a in enumerate(nums): 
            if i > 0 and a == nums[i-1]:
                continue
            l, r = i+1, len(nums) - 1
            while l < r:
                #  i, l       ,r    first loop, so -3 + -3 + 4 == 0?
                # [-3,-3,1,2,3,4]
                threeSum = a + nums[l] + nums[r]    
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
        