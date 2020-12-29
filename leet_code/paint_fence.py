"""
There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.
"""


class Solution:
    def numWays(self, n: int, k: int) -> int:
        # most concise
        # paint = [0, k, k**2]
        # for i in range(3, n + 1):
        #     paint.append((k - 1) * (paint[i - 1] + paint[i - 2]))
        # return paint[n]
        
        # better space complexity
        if n == 0:
            return 0
        if n == 1:
            return k
        prev2, prev1 = k, k**2
        for i in range(3, n + 1):
            prev2, prev1 = prev1, (k - 1) * (prev1 + prev2)
        return prev1

sol = Solution()
print(sol.numWays(3,2))