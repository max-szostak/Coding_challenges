"""
Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.
"""

class Solution:
    def threeSumSmaller(self, nums, target) -> int:
        def twoSumSmaller(left, target):
            count = 0
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] >= target:
                    right -= 1
                else:
                    count += right - left
                    left += 1
            return count
        
        nums = sorted(nums)
        count = 0
        for i in range(len(nums) - 2):
            count += twoSumSmaller(i + 1, target - nums[i]) 
        return count

sol = Solution()
print(sol.threeSumSmaller([-2,0,1,3], 2))