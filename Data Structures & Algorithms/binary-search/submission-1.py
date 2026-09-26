# search for 0
#  l    m     r
# [-1,0,2,4,6,8]
#  l  m r
# [-1,0,2,4,6,8]
# python divide is rounded down

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
        return -1