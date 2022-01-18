def devmod(x, y):
    return (x + y - 1) // y


def maina():

    N = int(input())
    print(devmod(N, 2) / N)


def mainb():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    print(sum(i >= K for i in h))


def mainc():
    N = int(input())
    A = list(map(int, input().split()))
    a = list(enumerate(A))
    a.sort(key=lambda x: x[1])
    ans = []
    for item in a:
        ans.append(item[0] + 1)
    print(*ans)


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


def maind():
    from math import gcd
    A, B = map(int, input().split())
    z = gcd(A, B)
    z = set(prime_factorize(z))
    print(len(z) + 1)


def maine():
    N, M = map(int, input().split())
    inf = 2 << 60
    C = []
    for i in range(M):
        a, b = map(int, input().split())
        c = list(map(lambda x: int(x) - 1, input().split()))
        C.append((a, c))
    dp = [inf for _ in range(1 << N)]
    dp[0] = 0
    for i in range(1 << N):
        for j in range(M):
            t = i
            a, c = C[j]
            for key in c:
                t = t | (1 << (key))
            dp[t] = min(dp[t], dp[i] + a)
    print(dp[-1] if dp[-1] != inf else -1)


maine()
