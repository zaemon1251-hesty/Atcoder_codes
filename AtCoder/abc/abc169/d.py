from typing import Counter


N = int(input())


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


def binaru_search(x):
    ok = 0
    ng = 10**9 + 1
    while ng-ok > 1:
        cen = (ng + ok)//2
        if cen * (cen + 1)//2 <= x:
            ok = cen
        else:
            ng = cen
    return ok


P = prime_factorize(N)
P = Counter(P)
ans = 0

for i in P.values():
    ans += binaru_search(i)
print(ans)
