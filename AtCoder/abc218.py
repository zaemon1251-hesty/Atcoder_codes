def mainc():
    N = int(input())
    S = set()
    T = set()

    def zerolize(P):
        mx, my = min(P)
        tmp = set()
        for x, y in P:
            tmp.add((x-mx, y-my))
        return tmp

    def rot(P):
        tmp = set()
        for x, y in P:
            tmp.add((y, -x))
        return tmp

    for i in range(N):
        A = list(input())
        for j in range(N):
            if A[j] == "#":
                S.add((i, j))
    for i in range(N):
        A = list(input())
        for j in range(N):
            if A[j] == "#":
                T.add((i, j))
    for _ in range(4):
        S = zerolize(S)
        T = zerolize(T)
        if S == T:
            print("Yes")
            exit()
        S = rot(S)
    else:
        print("No")


def maind():
    from collections import defaultdict
    N = int(input())
    S = defaultdict(set)
    for i in range(N):
        x, y = map(int, input().split())
        S[x].add(y)
    X = S.keys()
    ans = 0
    for x1 in X:
        for x2 in X:
            if x1 == x2:
                continue
            tmp = len(S[x1] & S[x2])
            ans += tmp*(tmp - 1)//2
    print(ans//2)


def maine():
    N, M = map(int, input().split())
    uf = UnionFind(N)
    G = [[] for _ in range(N)]
    R = []
    for i in range(M):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append((b, c))
        G[b].append((a, c))
        R.append((a, b, c))
    R.sort(key=lambda arr: arr[2], reverse=False)
    ans = 0
    for a, b, c in R:
        if uf.same(a, b):
            ans += max(c, 0)
        uf.union(a, b)
    print(ans)


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


maine()
