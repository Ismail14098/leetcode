# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# 0 1 2
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        i = -1
        while l <= r:
            m = int(r-l/2)
            if matrix[m][0] <= target and matrix[m][-1] >= target:
                i = m
                break
            elif matrix[m][-1] < target:
                l = m+1
            else:
                r = m-1
        if i == -1:
            return False
        l, r = 0, len(matrix[m])-1
        while l <= r:
            m = int(r-l/2)
            if matrix[i][m] == target:
                return True
            elif target > matrix[i][m]:
                l = m+1
            else:
                r = m-1
        return False

s = Solution()
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))