from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            if nums[l] < nums[m]:
                if target <= nums[m] and target >= nums[l]:
                    r = m-1
                else:
                    l = m+1
            elif nums[m] < nums[r]:
                if target >= nums[m] and target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
            elif l==r:
                return -1
        return -1

s = Solution()
print(s.search([3,1], 0))