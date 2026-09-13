# nums = [2,20,4,10,3,4,5]

# idea: turn nums -> set
# set = [2, 20, 4, 10, 3, 5]
# If you put the numbers in an x line, you'll notice that 2, 10, and 20
# doesn't have a left number that is exactly -1 of them (its 1, 9 and 19)
# So you could tell a start of a sequence using this technique.
# Now after you identify that a number doesnt have left number, e.g. 2
# you can iterate to the right until you dont find a number thats + 1 to get the longest sequence
# 2,3,4,5,   10,     20

# This way, you dont need to sort, hence O(n)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        current = 0
        longest = 0
        for n in num_set:
            if (n - 1) not in num_set:   # means that this is a start of a sequence
                current = 0     # bcs this is a start of a new sequence
                # check after 2 is 3? 2+1 == 3
                while (n + current) in num_set:     # check if 2 in num_set, then 3, 4, 5
                    current += 1
                longest = max(current, longest)
        return longest


        