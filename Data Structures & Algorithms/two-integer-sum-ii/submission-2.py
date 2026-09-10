# two pointers, O(n)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            currentTotal = numbers[left] + numbers[right]
            if currentTotal < target:
                left += 1
            elif currentTotal > target:
                right -= 1
            elif currentTotal == target:
                return [left+1, right+1]
