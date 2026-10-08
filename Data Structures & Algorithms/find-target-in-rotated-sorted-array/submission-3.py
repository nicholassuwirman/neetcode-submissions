# target = 1
#  l   m     r
# [3,4,5,6,1,2]
#        l m r
# [3,4,5,6,1,2]

# first compare if 5 == 1
# then compare 3 > 1, which is yes, means that
# no way that our target (1) is on the l-m side of the array, so move right

# target = 3
#  l   m     r
# [5,6,1,2,3,4]
#        l m r
# [5,6,1,2,3,4]

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = (l+r) // 2

            if target == nums[mid]:
                return mid
            # left sorted array
            if nums[l] <= nums[mid]:
                # make sure target is in between num[l] and nums[mid]
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # right sorted array
            else:
                # make sure target is in between num[mid] and nums[r]
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid -1
        return -1