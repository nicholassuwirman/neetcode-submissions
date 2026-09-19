#  
# [1,2,3,1]

# seen = {1:0, 2:1, 3:1}  value:position

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i in range(len(nums)):
            current_number = nums[i] 
            if current_number in seen:
                if abs(i-seen[current_number]) <= k:
                    return True

            seen[current_number] = i
        return False