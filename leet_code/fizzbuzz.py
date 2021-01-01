"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
"""

class Solution:
    def fizzBuzz(self, n: int):
        fizzdict = {3: "Fizz", 5: "Buzz"}
        strings = []
        for i in range(1, n + 1):
            s = ""
            for key in fizzdict:
                s += fizzdict[key] if i % key == 0 else ""
            if len(s) == 0:
                s = str(i)
            strings.append(s)
        return strings

sol = Solution()
print(sol.fizzBuzz(15))