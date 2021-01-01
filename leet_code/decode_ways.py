"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.
"""

class Solution:
    def numDecodings(self, s: str) -> int:   
        memo = {}
        def decode(s):
            if len(s) == 0:
                return 1
            if s[0] == '0':
                return 0
            if len(s) == 1:
                return 1
            if s in memo:
                return memo[s]
            r = decode(s[1:]) + (decode(s[2:]) if int(s[:2]) <= 26 else 0)
            memo[s] = r
            return r
        return decode(s)

sol = Solution()
print(sol.numDecodings("12"))