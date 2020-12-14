from fractions import Fraction
import sys

sys.setrecursionlimit(2000)

def expand_helper(n):
    if n == 0:
        return 2
    return 2 + Fraction(1, expand_helper(n - 1))

def expand(n):
    return 1 + Fraction(1, expand_helper(n - 1))

counter = 0

for i in range(1, 1001):
    exp = expand(i)
    if len(str(exp.numerator)) > len(str(exp.denominator)):
        counter += 1

print(counter)