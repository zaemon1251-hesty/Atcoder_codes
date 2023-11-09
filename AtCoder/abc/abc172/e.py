N, M = map(int, input().split())
MOD = 10**9 + 7


# 二項係数テーブル
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]
for i in range(2, M + 1):
    fact.append((fact[-1] * i) % MOD)
    inv.append((MOD - inv[MOD % i] * (MOD // i)) % MOD)
    factinv.append((factinv[i - 1] * inv[-1]) % MOD)


def cmb(n, k):
    # combination
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fact[n] * (factinv[k] * factinv[n - k] % MOD) % MOD


def pmb(n, k):
    # permutaition
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fact[n] * factinv[n - k] % MOD


ans = 0
op = 1
for k in range(N + 1):
    ans += pmb(M - k, N - k) * cmb(N, k) * op
    op *= -1
    ans %= MOD
ans *= pmb(M, N)
ans %= MOD
print(ans)
