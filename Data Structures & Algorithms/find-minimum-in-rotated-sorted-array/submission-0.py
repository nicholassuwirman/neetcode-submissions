#  l   m     r  
# [3,4,5,6,1,2]
#        l m r  
# [3,4,5,6,1,2]

#  l m   r
# [4,5,6,7]
#  m
#  l r
# [4,5,6,7]
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        smallest = nums[l]
        while l <= r:
            m = (l + r) // 2
            smallest = min(smallest, nums[m])

            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] <= nums[r]:
                r = m - 1
        return smallest
            