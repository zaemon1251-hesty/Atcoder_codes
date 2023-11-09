MOD = 10**9 + 7
S = int(input())
mg = S // 3
ans = 0

# 二項係数テーブル
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]
for i in range(2, S + 1):
    fact.append((fact[-1] * i) % MOD)
    inv.append((MOD - inv[MOD % i] * (MOD // i)) % MOD)
    factinv.append((factinv[i - 1] * inv[-1]) % MOD)


def cmb(n, k):
    # 二項係数テーブル
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fact[n] * (factinv[k] * factinv[n - k] % MOD) % MOD


for group in range(1, mg + 1):
    sep = group - 1
    ans += cmb(S - 3 * group + sep, sep)
    ans %= MOD
print(ans)
