import math
from PEF import ncr

counter = 0

for i in range(23, 101):
    for j in range(1, i):
        if ncr(i, j) > 10**6:
            counter += 1

print(counter)
