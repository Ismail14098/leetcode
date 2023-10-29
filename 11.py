from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        result = 0
        while l < r:
            result = max(min(height[l],height[r])*(r-l), result)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return result

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))