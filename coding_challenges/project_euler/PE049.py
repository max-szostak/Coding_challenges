from PEF import isPrime, isPerm

for i in range(1001, 10000, 2):
    for j in range(1001, 10000):
        terms = [i, i + j, i + j * 2]
        if terms[0] < 10000 and terms[1] < 10000 and terms[2] < 10000:
            if isPrime(terms[0]) and isPrime(terms[1]) and isPrime(terms[2]):
                if isPerm(terms[0], terms[1]) and isPerm(terms[0], terms[2]):
                    print(terms)
            




