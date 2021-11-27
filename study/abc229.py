def maina():
    s1 = list(input())
    s2 = list(input())
    s1 = [i for i in range(len(s1))if s1[i] == "#"]
    s2 = [i for i in range(len(s2))if s2[i] == "#"]
    if len(s1) == len(s2) == 1:
        if s1[0] != s2[0]:
            print("No")
            exit()
    print("Yes")


def mainb():
    A, B = map(int, input().split())
    while A and B:
        a, A = A % 10, A//10
        b, B = B % 10, B//10
        if a + b >= 10:
            print("Hard")
            exit()
    print("Easy")


def mainc():
    N, W = map(int, input().split())
    S = []
    for _ in range(N):
        a, b = map(int, input().split())
        S.append([a, b])
    S.sort(key=lambda x: x[0], reverse=True)
    i = 0
    ans = 0
    while W and i < N:
        t = min(S[i][1], W)
        ans += S[i][0] * t
        W -= t
        i += 1
    print(ans)


def maind():
    from itertools import accumulate
    S = list(input())
    S = [int(S[i] == ".") for i in range(len(S))]
    N = len(S)
    S = [0] + list(accumulate(S))
    K = int(input())
    ans = 0
    r = 0
    for l in range(N):
        while r < N and S[r+1] - S[l] <= K:
            r += 1
        ans = max(ans, r - l)
    print(ans)


maind()


def maine():
    N, M = map(int, input().split())
    S = []
    uf = UnionFind(N)
    used = [False] * M
    edf = {i: [] for i in range(N)}
    edge = []
    for i in range(M):
        a, b = map(int, input().split())
        edf[a-1].append(i)
        edge.append([a-1, b-1])
    ans = [0]
    for i in range(1, N)[::-1]:
        for j in edf[i]:
            if used[j]:
                continue
            a, b = edge[j]
            uf.union(a-1, b-1)
            used[j] = True
        ans.append(uf.gorup - i)
    print(*ans[::-1], sep="\n")


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.gorup = n

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
        self.gorup -= 1

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
