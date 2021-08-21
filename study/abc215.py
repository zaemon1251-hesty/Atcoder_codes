import math
from functools import reduce


def my_lcm_base(x, y):
    return (x * y) // math.gcd(x, y)


def my_lcm(*numbers):
    return reduce(my_lcm_base, numbers, 1)


def maina():
    s = input()
    if s == "Hello,World!":
        print("AC")
    else:
        print("WA")


def mainb():
    N = int(input())
    ok = 0
    ng = 60
    while ng - ok > 1:
        cen = (ok + ng) // 2
        if pow(2, cen) <= N:
            ok = cen
        else:
            ng = cen
    print(ok)


def mainc():
    from itertools import permutations
    S, K = map(str, input().split())
    S = permutations(list(S), len(S))
    S = set(S)
    A = []
    for item in list(S):
        y = ""
        for w in item:
            y += w
        A.append(y)

    A = sorted(A)
    # print(S)
    K = int(K)
    print(A[K-1])


def gcd(m, n):
    m, n = max(m, n), min(m, n)
    r = m % n
    return gcd(n, r) if r else n


def maind():
    n, m = list(map(int, input().split()))
    A = list(map(int, input().split()))

    def pFact(a):
        fctrz = []
        x = 2
        while x*x <= a:
            if a % x == 0:
                fctrz.append(x)
                while a % x == 0:
                    a //= x
            x += 1
        if a != 1:
            fctrz.append(a)
        return fctrz

    prints = []
    seive = [True]*(m+1)
    for k in A:
        fctrz = pFact(k)
        for p in fctrz:
            if p <= m and seive[p]:
                i_ = p
                while i_ <= m:
                    seive[i_] = False
                    i_ += p

    for i in range(1, m+1):
        if seive[i]:
            prints.append(i)

    print(len(prints))
    for p in prints:
        print(p)


def maine():
    mod = 998244353

    N = int(input())
    S = input()

    dp = [[0] * 10 for _ in range(1 << 10)]

    a = ord('A')
    cv = {c: ord(c) - a for c in "ABCDEFGHIJ"}

    for c in S:
        x = cv[c]
        # dp=前回の出場|不出場=今回の不出場
        # 今回の出場を加算していく

        # 過去に何らかのコンテストに出場していて
        # 最後にxに出場していたケース
        for bit in range(1 << 10):
            dp[bit][x] += dp[bit][x]
            dp[bit][x] %= mod

        # 過去に何らかのコンテストに出場していて
        # 初めてxに出場するケース
        for bit in range(1 << 10):
            if bit & (1 << x) > 0:
                continue  # xに出場していたら再度出場はできない
            for tail in range(10):
                dp[bit | (1 << x)][x] += dp[bit][tail]
                dp[bit | (1 << x)][x] %= mod

        # 初めて出場するケース
        dp[1 << x][x] += 1
        dp[1 << x][x] %= mod

    ans = 0
    for bit in range(1 << 10):
        for tail in range(10):
            ans += dp[bit][tail]
            ans %= mod
    print(ans)


maine()
