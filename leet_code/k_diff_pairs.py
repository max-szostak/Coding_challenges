""" 
Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i, j < nums.length
i != j
|nums[i] - nums[j]| == k
Notice that |val| denotes the absolute value of val.
"""

class Solution:
    def findPairs(self, nums, k) -> int:
        # brute force
        # if k == 0:
        #     nums = sorted(nums)
        #     dupes = set()
        #     for i in range(len(nums) - 1):
        #         if nums[i] == nums[i + 1]:
        #             dupes.add(nums[i])
        #     return len(dupes)
        # else:
        #     nums = sorted(list(set(nums)))
        #     count = 0
        #     while len(nums) > 0:
        #         i = nums[0]
        #         j = k + i
        #         if j in nums:
        #             count += 1
        #         nums.pop(0)
        #     return count
        
        # two pointer
        nums = sorted(nums)
        li = 0
        ri = 1
        counter = 0
        while li < len(nums) and ri < len(nums):
            if nums[ri] - nums[li] < k or li == ri:
                ri += 1
            elif nums[ri] - nums[li] > k:
                li += 1
            else:
                counter += 1
                temp = nums[li]
                li += 1
                while li < len(nums) and nums[li] == temp:
                    li += 1
        return counter

sol = Solution()
print(sol.findPairs([1,2,4,4,3,3,0,9,2,3], 3))