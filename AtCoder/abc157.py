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
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


class BIT:
    def __init__(self, Size):
        self.Size = Size
        self.Tree = [0] * (Size + 1)
        self.Depth = Size.bit_length() - 1

    def add(self, Index, Value):
        Index += 1
        while Index <= self.Size:
            self.Tree[Index] += Value
            Index += Index & -Index

    def query(self, L, R):
        ValueR = 0
        while R != 0:
            ValueR += self.Tree[R]
            R -= R & -R
        ValueL = 0
        while L != 0:
            ValueL += self.Tree[L]
            L -= L & -L
        return ValueR - ValueL


def maina():
    N = int(input())
    print((N + 1)//2)


def mainb():
    G = [list(map(int, input().split())) for _ in range(3)]
    N = int(input())
    b = {int(input()) for _ in range(N)}
    ans = "No"
    for i in range(3):
        if all(G[i][j] in b for j in range(3)):
            ans = "Yes"
        if all(G[j][i] in b for j in range(3)):
            ans = "Yes"
        if all(G[j][j] in b for j in range(3)):
            ans = "Yes"
    if all(t in b for t in (G[0][2], G[1][1], G[2][0])):
        ans = "Yes"
    print(ans)


def mainc():
    N, M = map(int, input().split())
    S = [list(map(int, input().split())) for _ in range(M)]
    for i in range(1000):
        w = str(i)
        if len(w) == N and all(w[s-1] == str(c) for s, c in S):
            print(w)
            return
    print(-1)


def maind():
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


def maine():
    N = int(input())
    BITs = [BIT(N) for _ in range(26)]
    S = list(map(lambda x: ord(x) - 97, input()))
    for i in range(N):
        BITs[S[i]].add(i, 1)
    Q = int(input())
    for _ in range(Q):
        T, X, Y = input().split()
        if T == '1':
            X = int(X) - 1
            Prev = S[X]
            Now = ord(Y) - 97
            S[X] = Now
            BITs[Prev].add(X, -1)
            BITs[Now].add(X, 1)
        else:
            X = int(X) - 1
            Y = int(Y)
            Ans = 0
            for i in range(26):
                Ans += BITs[i].query(X, Y) > 0
            print(Ans)


maine()
