"""
TODO
https://atcoder.jp/contests/abc247/submissions/30896431
"""


class UnionFind:
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
        return "\n".join("{}: {}".format(r, self.members(r)) for r in self.roots())


def main():
    MOD = 998244353
    N = int(input())
    uf = UnionFind(N)

    # F(n) = F(n-1) + F(n-2)
    F = [-1, 2, 3]
    for _ in range(N):
        F.append((F[-1] + F[-2]) % MOD)

    # G(n) = F(n-1) + F(n-3)
    G = [-1, 1, 3, 4] + [-1] * N
    for i in range(4, N + 1):
        G[i] = (F[i - 1] + F[i - 3]) % MOD

    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    for p, q in zip(P, Q):
        uf.union(p - 1, q - 1)

    ans = 1
    groups = [-i for i in uf.parents if i < 0]
    for g in groups:
        ans *= G[g]
        ans %= MOD
    print(ans)


if __name__ == "__main__":
    main()
