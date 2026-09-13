class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        l, r = 0, 1
        seen = False
        while r < len(nums):
            if nums[l] == nums[r]:
                seen = True
            l += 1
            r += 1
        return seen