""" You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top? """

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        memo = [-1] * (n + 1)
        memo[0] = 0
        memo[1] = 1 
        if n >= 2:
            memo[2] = 2
            
        def helper(n):
            if memo[n] != -1:
                return memo[n]
            result = helper(n-1) + helper(n-2)
            memo[n] = result
            return result
        
        return helper(n)

sol = Solution()
print(sol.climbStairs(10))