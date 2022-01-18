def maina():
    N, R = map(int, input().split())
    if N >= 10:
        ans = R
    else:
        ans = 100 * (10 - N) + R
    print(ans)


def mainb():
    N, K = map(int, input().split())
    i = 0
    while N >= K:
        N //= K
        i += 1
    print(i + 1)


def mainc():
    N = int(input())
    X = list(map(int, input().split()))
    a = sum(X) // N
    b = (sum(X) + N - 1) // N
    mina = sum((a - x)**2 for x in X)
    minb = sum((b - x)**2 for x in X)
    print(min(mina, minb))


def maind():
    n, a, b = map(int, input().split())
    mod = 10**9+7

    def cmb(n, r):
        r = min(n-r, r)  # nCrでもnCn-rでも一緒のことなので小さい方を取ることで高速化を図る
        a = 1
        b = 1
        for k in range(r):
            a *= (n-r+1+k)
            a %= mod
            b *= (k+1)
            b %= mod
        return a * pow(b, mod-2, mod) % mod
    print((pow(2, n, mod) - 1 - cmb(n, a) - cmb(n, b)) % mod)


def maine():
    N, K = map(int, input().split())
    K = min(K, N-1)
    MOD = 10**9+7

    # 二項係数テーブル
    fact = [1, 1]
    factinv = [1, 1]
    inv = [0, 1]
    for i in range(2, N+1):
        fact.append((fact[-1]*i) % MOD)
        inv.append((MOD-inv[MOD % i]*(MOD//i)) % MOD)
        factinv.append((factinv[i-1]*inv[-1]) % MOD)

    # 二項係数テーブル
    def cmb(n, k):
        if n < k:
            return 0
        if n < 0 or k < 0:
            return 0
        return fact[n]*(factinv[k]*factinv[n-k] % MOD) % MOD

    Ans = 0
    for i in range(K+1):
        Ans = (Ans+cmb(N, i)*cmb(N-1, i)) % MOD
    print(Ans)


maine()
