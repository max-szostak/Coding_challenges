"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
"""

class Solution:
    def maximalSquare(self, matrix) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)] 
        maxside = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1): 
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxside = max(maxside, dp[i][j])
        return maxside ** 2

sol = Solution()
print(sol.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))