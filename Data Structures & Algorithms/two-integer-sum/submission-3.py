

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in seen:
                seen[nums[i]] = i
            else:
                return [seen[diff], i]