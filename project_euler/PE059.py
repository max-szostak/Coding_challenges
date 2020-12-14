from itertools import product 
from itertools import cycle

enc_file = open("PE059_encrypted.txt", "r")
enc = enc_file.readlines()[0]

nums = []
current = ""
for c in enc:
    if c == ",":
        nums.append(int(current))
        current = ""
    else:
        current += c
nums.append(int(current))

keys = list(product(range(97, 123), repeat = 3))
for key in keys:
    dec = [chr(a ^ b) for (a, b) in zip(nums, cycle(key))]
    dec = "".join(dec)
    if "the" in dec and "be" in dec and "to" in dec and "extract taken" in dec: 
        final = dec

sum = 0
for c in final:
    sum += ord(c)
print(sum)


