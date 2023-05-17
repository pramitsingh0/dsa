import math


def isPrime(n):
    i = 2
    while i < math.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True

print(isPrime(5))
