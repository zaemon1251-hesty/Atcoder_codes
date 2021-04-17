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
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


N, M, K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
CD = [list(map(int, input().split())) for _ in range(K)]

uf = UnionFind(N)
friend = [0]*N
blocked = [0]*N

for a, b in AB:
    uf.union(a-1, b-1)
    friend[a-1] += 1
    friend[b-1] += 1

for c, d in CD:
    if uf.same(d-1, c-1):
        blocked[c-1] += 1
        blocked[d-1] += 1

ans = [uf.size(i)-friend[i]-blocked[i]-1 for i in range(N)]
print(' '.join(map(str, ans)))