import sys


def input():
    return sys.stdin.readline().rstrip()


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


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())


def aising2019_c():
    from itertools import product

    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())
    H, W = mi()
    S = [input() for _ in range(H)]
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    uf = UnionFind(H * W)

    for x, y in product(range(H), range(W)):
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 0-indexで考える
            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                continue
            if S[nx][ny] == S[x][y]:
                continue
            if not uf.same(W * x + y, W * nx + ny):
                uf.union(W * x + y, W * nx + ny)
    ans = 0
    g = {r: [0, 0] for r in uf.roots()}
    for x, y in product(range(H), range(W)):
        g[uf.find(W * x + y)][S[x][y] == "."] += 1

    for b, w in g.values():
        ans += b * w
    print(ans)


def arc092_a():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N = ii()

    A = [li() for _ in range(N)]
    B = [li() for _ in range(N)]

    A.sort(key=lambda x: (x[0], x[1]))
    B.sort(key=lambda x: (x[0], x[1]))

    ans = 0
    for bx, by in B:
        tmp = -1
        idx = -1
        for i, (rx, ry) in enumerate(A):
            if rx < bx and tmp < ry < by:
                tmp = ry
                idx = i
        if tmp != -1:
            ans += 1
            A = [a for i, a in enumerate(A) if i != idx]

    print(ans)


def arc097_b():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N, M = mi()
    P = li()
    S = [li() for _ in range(M)]
    uf = UnionFind(N)
    for x, y in S:
        if not uf.same(x - 1, y - 1):
            uf.union(x - 1, y - 1)

    ans = 0
    for i in range(N):
        if uf.same(i, P[i] - 1):
            ans += 1

    print(ans)


def arc125_b():
    from math import sqrt
    MOD = 998244353

    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N = ii()
    ans = 0
    for q in range(1, int(sqrt(N)) + 1):
        ans += (N // q - q + 1) // 2
        ans += (N // q) % 2 == q % 2
        ans %= MOD
    print(ans)


def m_solutions2019_d():
    import sys
    sys.setrecursionlimit(10**6)

    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N = ii()

    G = [[] for _ in range(N)]

    for _ in range(N - 1):
        a, b = mi()
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)

    c = sorted(li(), reverse=True)
    w = [-1] * N
    i_ = [0]

    def dfs(v, p):
        res = 0
        for nv in G[v]:
            if nv != p:
                w[nv] = c[i_[0]]
                i_[0] += 1
                res += w[nv] + dfs(nv, v)
        return res

    w[0] = c[i_[0]]
    i_[0] += 1

    print(dfs(0, -1))
    print(*w)


if __name__ == '__main__':
    m_solutions2019_d()
