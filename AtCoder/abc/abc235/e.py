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


N, M, Q = map(int, input().split())
E = []
ans = ["No"] * Q
uf = UnionFind(N)
for i in range(M):
    a, b, c = map(int, input().split())
    E.append((a - 1, b - 1, c, -1))
for i in range(Q):
    u, v, w = map(int, input().split())
    E.append((u - 1, v - 1, w, i))
E.sort(key=lambda x: x[2])

for i in range(M + Q):
    x, y, w, q = E[i]
    if q == -1:
        uf.union(x, y)
    else:
        if not uf.same(x, y):
            ans[q] = "Yes"
print(*ans, sep="\n")
