class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        buf = 1
        for i in range(len(nums)):
            result[i] = buf
            buf *= nums[i]
        buf = 1
        for i in reversed(range(len(nums))):
            result[i] *= buf
            buf *= nums[i]
        return result