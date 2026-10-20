# target = 3
# [1,2,3,4]
#  l 
#         r 
# 
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l != r:
            current_total = numbers[l] + numbers[r]
            if current_total == target:
                return [l+1, r+1]
            elif current_total > target:
                r -= 1
            elif current_total < target:
                l += 1
        return []