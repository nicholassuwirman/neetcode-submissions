class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat_list = [num for row in matrix for num in row]
        l = 0
        r = len(flat_list) - 1
        while l <= r:
            m = (l + r) // 2
            if flat_list[m] == target:
                return True
            elif target < flat_list[m]:
                r = m - 1
            else: 
                l = m + 1
        return False