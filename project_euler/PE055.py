from PEF import isPal

def reverse(n):
    return int(str(n)[::-1])

counter = 10000
for n in range(1, 10001):
    found = False
    its = 0
    i = n
    while not found and its < 50:
        new = i + reverse(i)
        if isPal(new):
            found = True
            counter -= 1
        else:
            i = new
        its += 1

print(counter)


