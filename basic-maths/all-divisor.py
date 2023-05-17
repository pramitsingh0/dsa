import math
def all_divisors(n):
    i = 1
    while i < math.sqrt(n):
        if n % i == 0:
            print(i, int(n / i))
        i += 1

print(all_divisors(36))
