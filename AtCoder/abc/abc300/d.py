from math import isqrt

N = int(input())

# sqrt(N) 以下の素数の列挙
sieve = [1] * (isqrt(N) + 1)
primes = []
for p in range(2, len(sieve)):
    if sieve[p] == 0:
        continue
    primes.append(p)
    for j in range(p * p, len(sieve), p):
        sieve[j] = 0

# prefix_sum[n] : (n 以下の素数の個数)
prefix_sum = sieve
for i in range(len(prefix_sum) - 1):
    prefix_sum[i + 1] += prefix_sum[i]

ans = 0

# a, b を全探索する
for i in range(len(primes)):
    a = primes[i]
    if a * a * a * a * a >= N:
        break
    for j in range(i + 1, len(primes)):
        b = primes[j]
        if a * a * b * b * b >= N:
            break
        ans += prefix_sum[isqrt(N // (a * a * b))] - prefix_sum[b]
print(ans)
