from itertools import combinations, product
from functools import reduce, lru_cache


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


def arc107_c():
    MOD = 998244353

    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())
    N, K = mi()

    @lru_cache(None)
    def exlp(n):
        if n == 0:
            return 1

        return (n * exlp(n - 1)) % MOD

    A = [li() for _ in range(N)]

    uf1 = UnionFind(N)
    uf2 = UnionFind(N)

    for i, j in combinations(range(N), 2):
        if all(A[i][x] + A[j][x] <= K for x in range(N)):
            uf1.union(i, j)
        if all(A[x][i] + A[x][j] <= K for x in range(N)):
            uf2.union(i, j)

    ans = 1

    rows = [-uf1.parents[i] for i in range(N) if uf1.parents[i] < 0]
    cols = [-uf2.parents[i] for i in range(N) if uf2.parents[i] < 0]

    for y in rows:
        ans *= exlp(y)
        ans %= MOD
    for y in cols:
        ans *= exlp(y)
        ans %= MOD

    print(ans)


def agc048_a():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    INF = 10**18

    T = ii()

    def solve():
        S = input()
        ans = INF
        if all(s == "a" for s in S):
            print(-1)
            return
        if S > "atcoder":
            print(0)
            return

        for i, s in enumerate(S):
            if s == "a":
                continue
            if s > "t":
                ans = min(ans, i - 1)
            else:
                ans = min(ans, i)

        print(ans if ans < INF else -1)

    for _ in range(T):
        solve()


if __name__ == "__main__":
    agc048_a()
