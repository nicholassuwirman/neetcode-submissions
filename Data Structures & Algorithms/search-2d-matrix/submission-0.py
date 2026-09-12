#              l   r  m     r
# flat_list = [1,2,4,8,10,11,...]
# use binary search for the flat_list

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat_list = [num for row in matrix for num in row]
        l, r = 0, len(flat_list) - 1
        while l <= r:
            m = (l + r) // 2
            if flat_list[m] == target:
                return True
            elif flat_list[m] < target:
                l = m + 1
            elif flat_list[m] > target:
                r = m - 1
        return False