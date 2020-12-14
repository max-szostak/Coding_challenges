""" Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory."""

class Solution:
    def removeDuplicates(self, nums) -> int:
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                nums.pop(j)
            else:
                i += 1
                j += 1
        return len(nums)

sol = Solution()
print(sol.removeDuplicates([1,1,1,2,2,3,4,5,5,5,5]))