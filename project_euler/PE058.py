from PEF import isPrime

diags = [1]
primes = 0
counter = 1
found = False
inc = 2


while not found:
    # print(primes)
    # print(len(diags))
    for i in range(0, 4):
        counter += inc
        if isPrime(counter):
            primes += 1
        diags.append(counter)
    if primes / len(diags) < 0.1:
        print(inc + 1)
        found = True
    inc += 2

