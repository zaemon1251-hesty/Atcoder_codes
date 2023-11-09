import sys


def input():
    return sys.stdin.readline().rstrip()


class ModCmb:
    """calc combinations on the conditions of a certain mod"""

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
        return self.fact[n] * (self.factinv[k] * self.factinv[n - k] % self.MOD) % self.MOD


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N, M, K = mi()
    MOD = 10**9 + 7
    mods = ModCmb(N * M, MOD)

    ans = 0
    for d in range(1, N):
        ans += d * (N - d) * M**2
        ans %= MOD

    for d in range(1, M):
        ans += d * (M - d) * N**2
        ans %= MOD

    ans *= mods.cmb(M * N - 2, K - 2)
    ans %= MOD

    print(ans)


if __name__ == "__main__":
    main()
