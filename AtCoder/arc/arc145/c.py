N = int(input())

MOD = 998244353

# 二項係数テーブル
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]
for i in range(2, 2 * N + 1):
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


def main():
    print(pow(2, N, MOD) * fact[2 * N] * factinv[N + 1] % MOD)


if __name__ == "__main__":
    main()
