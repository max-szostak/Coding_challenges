""" Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order. """

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # brute force solution
        # for x in range(0, len(nums)):
        #     for y in range (x + 1, len(nums)):
        #         if nums[x] + nums[y] == target:
        #             return [x,y]
                
        # hashing solution
        numdict = {nums[i]: i for i in range(0, len(nums))}
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in numdict and numdict[diff] != i:
                return [i, numdict[diff]]

sol = Solution()
print(sol.twoSum([2,7,11,15],9))

        