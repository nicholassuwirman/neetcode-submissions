# nums = [3,4,5,6], target = 7
# target - 3 = 4, so we only need to know if 4 exist
# put nums into a hashmap, check if 4 in hashmap

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_nums = {}  # value : index, e.g. 3:0, 4:1, 5:2

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in hash_nums:
                hash_nums[nums[i]] = i
            else:
                return [hash_nums[diff], i]

        
        