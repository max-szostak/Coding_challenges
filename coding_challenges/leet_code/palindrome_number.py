""" Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Follow up: Could you solve it without converting the integer to a string? """

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        # easy solution: convert to string
        # xstr = str(x)
        # return xstr == xstr[::-1]
    
        # more interesting: without converting
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        rev = 0
        while x > rev:
            rev *= 10
            rev += x % 10
            x = x // 10
        return rev == x or rev // 10 == x

sol = Solution()
print(sol.isPalindrome(12321))