"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        memo = set()
        def isPal(s):
            if len(s) <= 1:
                return True
            elif s[0] != s[len(s) - 1]:
                return False
            elif s in memo:
                return True
            else:
                return isPal(s[1:len(s) - 1])        
        count = len(s)
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                sub = s[i:j + 1]
                if isPal(sub):
                    count += 1
                    memo.add(sub)
        return count

sol = Solution()
print(sol.countSubstrings("aaa"))