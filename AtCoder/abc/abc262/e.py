class ModCmb:
    """calc combinations on the conditions of a certain mod
    """

    def __init__(self, N, mod=10**9 + 7):
        # 二項係数テーブル
        fact = [1, 1]
        factinv = [1, 1]
        inv = [0, 1]
        for i in range(2, N + 1):
            fact.append((fact[-1] * i) % mod)
            inv.append((mod - inv[mod % i] * (mod // i)) % mod)
            factinv.append((factinv[i - 1] * inv[-1]) % mod)

        # 初期化
        self.MOD = mod
        self.N = N
        self.fact = fact
        self.factinv = factinv
        self.inv = inv

    def cmb(self, n, k):
        if n < k:
            return 0
        if n < 0 or k < 0:
            return 0
        return self.fact[n] * \
            (self.factinv[k] * self.factinv[n - k] % self.MOD) % self.MOD


def main():
    MOD = 998244353
    N, M, K = map(int, input().split())
    E = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]
    G = [[]for _ in range(N)]
    for u, v in E:
        G[u].append(v)
        G[v].append(u)

    odds = 0
    for i in range(N):
        odds += len(G[i]) % 2
    evens = N - odds
    ans = 0
    bitable = ModCmb(N, MOD)
    for oddnum in range(0, min(odds, K) + 1, 2):
        if K - oddnum <= evens:
            ans += bitable.cmb(odds, oddnum) * bitable.cmb(evens, K - oddnum)
            ans %= MOD

    print(ans)


if __name__ == '__main__':
    main()
