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


def mainc():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    Z = []
    for i, s in enumerate(T):
        Z.append((i, s))
    Z = sorted(Z, key=lambda x: x[1], reverse=True)
    ans = [-1] * N
    y, t = Z.pop()
    cnt = 0
    while cnt < N:
        n_y = (y + 1) % N
        if t + S[y] <= T[n_y]:
            ans[n_y] = t + S[y]
            t += S[y]
        else:
            ans[n_y] = T[n_y]
            t = T[n_y]
        y = n_y
        cnt += 1
    print(*ans, sep='\n')


def maind():
    inf = 10e+9
    N = int(input())
    uf = UnionFind(N)
    e = []
    for i in range(N - 1):
        st, en, w = map(int, input().split())
        e.append((st-1, en-1, w))
    e.sort(key=lambda x: x[2], reverse=True)

    ans = 0
    while e:
        a, b, w = e.pop()
        ans += uf.size(a) * uf.size(b) * w
        uf.union(a, b)
    print(ans)


maind()
