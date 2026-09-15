# optimal O n solution based on neetcode vid
# nums = [1,2,4,6]
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # initialize an array
        # use the res array also as a container for prefix (iterate 0 to n)
        # then directly compute postfix (iterate n-1 to 0) -> result in this res array 
        res = [1] * (len(nums))     # initialize an array, use the 

        prefix = 1
        # first calculate prefix, put those in res array
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        # [1,1,2,8]     // these are prefixes from [1,2,4,6]

        postfix = 1
        # this is how you loop down in python
        #                  start  ,stop,step
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix   # if you do rest[i] = postfix then you're overriding the values
            postfix *= nums[i]
        
        return res
