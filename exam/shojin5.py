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


if __name__ == '__main__':
    aising2019_c()
