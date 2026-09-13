# O n log n
# nums = [2,20,4,10,3,4,5]

# idea: hash map, sort the hashmap, loop if hashmap[i] = hashmap[i] + 1
# hash_nums = [2:1, 20:1, 4:2, 10:1, 3:1, 5:1]
# sorted_nums = sort(hash_nums)
# sorted_nums = [2:1,3:1,4:2,5:1,10:1,20:1]
# current = 0, longest = 0
# iterate sorted nums, if current value+1 == next value, current+= 1, else return
# check also longest = max(longest, current)
# return longest

# careful of cases such as [0,1,3,4,5], if you prematurely return from the 1,3 jump
# then you'll miss the correct answer which is 3 (3,4,5 sequence)

# Input: nums = [0,3,2,5,4,6,1,1]
# [0,1,1,2,3,4,5,6]
# double number or more than 1 same number arent counted as the output

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        hash_nums = {}
        
        for i in range(len(nums)):
            hash_nums[nums[i]] = hash_nums.get(nums[i], 0) + 1
        
        #                   (sort hash_nums, sort based on key, ascending)
        sorted_nums = sorted(hash_nums.items(), key=lambda pair:pair[0], reverse=False)

        current = 1
        longest = 1
        
        for j in range(len(sorted_nums) - 1):
            if sorted_nums[j][0] + 1 == sorted_nums[j+1][0]:
                current +=1
            else:
                current = 1
            longest = max(longest, current)

        return longest
                