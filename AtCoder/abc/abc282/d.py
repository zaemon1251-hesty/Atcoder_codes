import sys

sys.setrecursionlimit(10**6)


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


def input():
    return sys.stdin.readline().rstrip()


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N, M = mi()
    G = [[] for _ in range(N)]
    uf = UnionFind(N)
    for _ in range(M):
        u, v = mi()
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)

        if not uf.same(u, v):
            uf.union(u, v)

    bw = {i: [0, 0] for i in range(N)}
    cols = [-1] * N

    def dfs(v, f):
        cols[v] = f
        for nv in G[v]:
            if cols[nv] != -1:
                if cols[nv] == f:
                    return False
                continue

            if not dfs(nv, 1 - f):
                return False

        return True

    for i in range(N):
        if cols[i] != -1:
            continue
        enable = dfs(i, 0)
        if not enable:
            print(0)
            return

    for i, c in enumerate(cols):
        bw[uf.find(i)][c == 0] += 1

    ans1 = 0
    ans2 = 0
    for black, white in bw.values():
        if black == white == 0:
            continue
        ans1 += black * white
        ans2 += (black + white) * (N - black - white)
    print(ans1 - M + ans2 // 2)


if __name__ == "__main__":
    main()
