class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]
        self.height = [1] * n
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.height[x] < self.height[y]:
                self.parent[x] = y
                self.size[y] += self.size[x]
            else:
                self.parent[y] = x
                self.size[x] += self.size[y]
                if self.height[x] == self.height[y]:
                    self.height[x] += 1

    def issame(self, x, y):
        return self.find(x) == self.find(y)

    def group_size(self, x):
        return self.size[self.find(x)]

    def group_members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parent) if i == x]

    def group_count(self):
        return len(self.roots())


N = 4
A = [tuple(map(int, input().split())) for _ in range(N)]


def grid2int(x, y, n):
    return x + y * n


def isOK(b):
    table = [[0] * (N + 2) for _ in range(N + 2)]
    for x in range(N):
        for y in range(N):
            i = grid2int(x, y, N)
            table[x + 1][y + 1] = int((b >> i) & 1)

    # 全ての村を含んでいるか
    for x in range(N):
        for y in range(N):
            if A[x][y] == 1 and table[x + 1][y + 1] == 0:
                return False

    # 連結成分数が2 (内と外) だけか
    uf = UnionFind((N + 2) ** 2)
    for x in range(N + 2):
        for y in range(N + 1):
            if table[x][y] == table[x][y + 1]:
                uf.unite(grid2int(x, y, N + 2), grid2int(x, y + 1, N + 2))
    for x in range(N + 1):
        for y in range(N + 2):
            if table[x][y] == table[x + 1][y]:
                uf.unite(grid2int(x, y, N + 2), grid2int(x + 1, y, N + 2))

    return uf.group_count() == 2


ans = 0
for b in range(1 << (N**2)):
    ans += isOK(b)
print(ans)
