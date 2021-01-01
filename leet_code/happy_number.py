"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        
        def nextNum(n):
            r = 0 
            while n > 0:
                r += (n % 10) ** 2
                n = n // 10
            return r
        
        # using hashmap -- slightly slower runtime
        # seen = {}
        # while n not in seen:
        #     seen[n] = True
        #     n = nextNum(n)
        #     if n == 1:
        #         return True
        # return False

        # using two pointer
        slow = n
        fast = nextNum(n)
        while fast != 1 and slow != fast:
            slow = nextNum(slow)
            fast = nextNum(nextNum(fast))
        return fast == 1
        
sol = Solution()
print(sol.isHappy(19))
        