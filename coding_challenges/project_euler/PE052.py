from PEF import isPerm

done = False
i = 125874
while not done:
    i += 1
    mults = [i * n for n in range(2, 7)]
    candidate = True
    for j in mults:
        if not isPerm(i, j):
            candidate = False
    done = candidate

print(i)
