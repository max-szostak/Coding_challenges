"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
"""

class Solution:
    def maxSubArray(self, nums) -> int:
        currentsum = maxsum = nums[0]
        for i in range(1, len(nums)):
            currentsum = max(currentsum + nums[i], nums[i])
            maxsum = max(maxsum, currentsum)
        return maxsum

sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))