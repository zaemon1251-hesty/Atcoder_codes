K = int(input())
S = input()
N = len(S)
MOD = 10**9 + 7
# 二項係数テーブル
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]
for i in range(2, N + K + 1):
    fact.append((fact[-1] * i) % MOD)
    inv.append((MOD - inv[MOD % i] * (MOD // i)) % MOD)
    factinv.append((factinv[i - 1] * inv[-1]) % MOD)
# 二項係数テーブル


def cmb(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fact[n] * (factinv[k] * factinv[n - k] % MOD) % MOD


ans = 0
for k in range(K + 1):
    ans += cmb(N + K, k) * pow(25, k, MOD)
    ans %= MOD
print(ans)
