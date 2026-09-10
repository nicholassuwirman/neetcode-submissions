# Sorted approach, n log n
# bcs sort() WC is O(n log n), loop itself is O(n)
# BC if the array/list is already sorted, hence O(n)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        max = len(nums)
        for i in range(max-1):
            if nums[i] == nums[i+1]:
                return True
        return False