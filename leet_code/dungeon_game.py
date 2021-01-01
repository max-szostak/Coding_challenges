"""
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

 

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.
"""

class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[0] * n for _ in range(m)]
        dp[m - 1][n - 1] = max(1 - dungeon[m - 1][n - 1], 1)
        for i in range(m - 2, -1, -1):
            dp[i][n - 1] = max(dp[i + 1][n - 1] - dungeon[i][n - 1], 1)
        for j in range(n - 2, -1, -1):
             for i in range(m - 1, -1, -1):
                    if i == m - 1:
                        dp[i][j] = max(dp[i][j + 1] - dungeon[i][j], 1)
                    else:
                        down = dp[i + 1][j]
                        right = dp[i][j + 1]
                        h = min(down, right) - dungeon[i][j]
                        dp[i][j] = max(h, 1)
        return dp[0][0]

sol = Solution()
print(sol.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))