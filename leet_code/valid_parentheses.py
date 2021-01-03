"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""
import collections 

class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', '}': '{', ']': '['}
        stack = collections.deque()
        for c in s:
            if c in pairs:
                top = stack.pop() if stack else ""
                if top != pairs[c]:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0

sol = Solution()
print(sol.isValid("{[]}"))