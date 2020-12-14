from PEF import atkin, isPrime

primes = atkin(10**6)

max = 0
max_sum = 0
for i in range(0, len(primes)):
    sum = 0
    j = i + 1
    while j < len(primes) and sum < 10**6:
        sum += primes[j]
        if isPrime(sum):
            if j - i > max:
                max = j - i
                max_sum = sum
        j += 1


print(max_sum)

    

