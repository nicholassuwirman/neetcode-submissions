# O n log n
# nums = [2,20,4,10,3,4,5]

# idea: set, sort the set, loop if set[i] = set[i] + 1
# set = [2, 20, 4, 10, 3, 5]
# sorted_set = [2,3,4,5,10,20]

# careful of cases such as [0,1,3,4,5], if you prematurely return from the 1,3 jump
# then you'll miss the correct answer which is 3 (3,4,5 sequence)

# Input: nums = [0,3,2,5,4,6,1,1]
# [0,1,1,2,3,4,5,6]
# double number or more than 1 same number arent counted as the output

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sorted_nums = sorted(set(nums))

        longest = 1
        current = 1

        for j in range(len(sorted_nums) - 1):
            # checks is the numer on sorted_nums[j]'s right + 1?
            # say its 2, it checks if 2 + 1 == 3
            if sorted_nums[j] + 1 == sorted_nums[j + 1]:
                current += 1
            else:
                current = 1
            longest = max(longest, current)

        return longest
                