from math import gcd
A, B = map(int, input().split())
z = gcd(A, B)
z = set(prime_factorize(z))
print(len(z) + 1)
