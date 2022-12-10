import sys


def input():
    return sys.stdin.readline().rstrip()


MOD = 998244353


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r))
                         for r in self.roots())


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
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N, M = mi()
    P = li()
    i = 0
    uf = UnionFind(N)
    for i, p in enumerate(P):
        uf.union(i, p - 1)

    C = len(uf.roots())

    print((pow(M, N, MOD) - pow(M, C, MOD)) * pow(2, MOD - 2, MOD) % MOD)


if __name__ == '__main__':
    main()
