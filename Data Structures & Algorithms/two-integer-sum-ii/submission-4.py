# 1-indexed
# 1, 2, 3, 4
# l       r
# 9,10,20,30,40 target = 29
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l != r:
            if (numbers[l] + numbers[r]) == target:
                return [l+1, r+1]
            elif (numbers[l] + numbers[r]) < target: 
                l+=1
            elif (numbers[l] + numbers[r]) > target: 
                r-=1