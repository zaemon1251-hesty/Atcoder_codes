from functools import lru_cache
M = 998244353
d = pow(5, -1, M)
n = int(input())


@lru_cache(None)
def f(k):
    if k >= n:
        return k == n
    return sum(f(k*x) for x in range(2, 7))*d % M


print(f(1))
