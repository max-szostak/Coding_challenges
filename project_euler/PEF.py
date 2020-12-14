import math

def atkin(nmax):
    """
    Returns a list of prime numbers below the number "nmax"
    """
    is_prime = dict([(i, False) for i in range(5, nmax+1)])
    for x in range(1, int(math.sqrt(nmax))+1):
        for y in range(1, int(math.sqrt(nmax))+1):
            n = 4*x**2 + y**2
            if (n <= nmax) and ((n % 12 == 1) or (n % 12 == 5)):
                is_prime[n] = not is_prime[n]
            n = 3*x**2 + y**2
            if (n <= nmax) and (n % 12 == 7):
                is_prime[n] = not is_prime[n]
            n = 3*x**2 - y**2
            if (x > y) and (n <= nmax) and (n % 12 == 11):
                is_prime[n] = not is_prime[n]
    for n in range(5, int(math.sqrt(nmax))+1):
        if is_prime[n]:
            ik = 1
            while (ik * n**2 <= nmax):
                is_prime[ik * n**2] = False
                ik += 1
    primes = []
    for i in range(nmax + 1):
        if i in [0, 1, 4]: pass
        elif i in [2,3] or is_prime[i]: primes.append(i)
        else: pass
    return primes

def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for m in range(3, int(math.sqrt(n)) + 1):
        if n % m == 0:
            return False
    return True

def isPerm(a, b):
    ## returns true if a is a permuation of b
    a = str(a)
    b = str(b)
    for c in a:
        if len(b) == 0 or (len(b) == 1 and b[0] == c):
            return True
        i = b.find(c)
        if i >= 0:
            b = b[:i] + b[i + 1:]
        else:
            return False

def nextPrime(n):
    ## returns the first prime number in the interval (n, inf)
    n += 1
    if n % 2 == 0:
        n += 1
    while not isPrime(n):
        n += 2
    return n

def ncr(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))

def isPal(n):
    ## returns true if n is a palindrome number
    n = str(n)
    split = int(len(n) / 2)
    left = n[:split]
    if len(n) % 2 == 0:
        right = n[split:]
    else:
        right = n[split + 1:]
    right = right[::-1]
    return left == right

def gcd(a, b):
    ## returns the greatest common denominator of a and b
    if a == 0:
        return int(b)
    else:
        return int(gcd(b % a, a))

