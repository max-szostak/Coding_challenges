def addDigs(n):
    n = str(n)
    sum = 0
    for c in n:
        sum += int(c)
    return sum

max = 0

for a in range(1, 100):
    for b in range(1, 100):
        sum = addDigs(a ** b)
        if sum > max:
            max = sum

print(max)

