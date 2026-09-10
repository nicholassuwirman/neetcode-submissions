# Prefix Sum / Prefix Product pattern
# O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        maxLen = len(nums)
        resultList = []
        leftList = [1] * maxLen
        rightList = [1] * maxLen
        for i in range(1, maxLen):
            leftList[i] = leftList[i-1] * nums[i-1]
        for y in range(maxLen-2, -1, -1):
            rightList[y] = rightList[y+1] * nums[y+1]
        for x in range(maxLen):
            product = 1
            product = leftList[x] * rightList[x]
            resultList.append(product)
        return resultList

         