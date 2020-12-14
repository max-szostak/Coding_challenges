from PEF import isPrime
from itertools import combinations
from itertools import permutations


done = False
len = 4

while not done and len < 6:
    for end_num in range(0, 10):
        if done:
            break
        for num_stars in range(1, len + 1):
            num_ranger = len - num_stars
            for ranger_list in combinations(range(0, 10), num_ranger):
                base = "*" * num_stars
                for i in ranger_list:
                    base = base + str(i)
                for perm in set(permutations(base)):
                    perm = list(perm)
                    prime_counter = 0
                    first_prime = 0
                    for i in range(0, 10):
                        final = [i if c == "*" else int(c) for c in perm]
                        final.append(end_num)
                        final = int(''.join(map(str, final))) ## converting list of ints to one concatenated int
                        if isPrime(final):
                            prime_counter += 1
                            if first_prime == 0:
                                first_prime = final
                    if prime_counter == 8:
                        print(first_prime)
                        done = True
    len += 1

