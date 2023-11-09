# BIT : Fenwick Tree : max 用に修正
# 使用側 1_indexed, 実装側 1_indexed
# __setitem__: obj[p] = x -> [p] = op([p], x)
# __getitem__: obj[r] -> return op[1,r]
class FenwickTree:
    def __init__(self, n, e, op):
        self.n = n  # [1,n], 1_indexed
        self.e = e
        self.op = op
        self.fw = [e] * (n + 1)  # FW tree, 1_indexed

    def __setitem__(self, p, x):
        while p <= self.n:
            self.fw[p] = self.op(self.fw[p], x)
            p += p & -p

    def __getitem__(self, r):
        s = self.e
        while r:
            s = self.op(s, self.fw[r])
            r -= r & -r
        return s


def solve():
    INF = float("inf")
    N = int(input())
    P = [*map(int, input().split())]

    D = [INF] * N

    # j<i & pj<pi
    fw = FenwickTree(N, -INF, max)
    for i in range(N):
        pi = P[i]
        mn = pi + i - fw[pi - 1]
        D[i] = min(D[i], mn)
        fw[pi] = pi + i

    # j>i & pj<pi
    fw = FenwickTree(N, -INF, max)
    for i in range(N - 1, -1, -1):
        pi = P[i]
        mn = pi - i - fw[pi - 1]
        D[i] = min(D[i], mn)
        fw[pi] = pi - i

    # j<i & pj>pi
    fw = FenwickTree(N, -INF, max)
    for i in range(N):
        pi = P[i]
        mn = (N - fw[N - pi]) - (pi - i)
        D[i] = min(D[i], mn)
        fw[N + 1 - pi] = N - (pi - i)

    # j>i & pj>pi
    fw = FenwickTree(N, -INF, max)
    for i in range(N - 1, -1, -1):
        pi = P[i]
        mn = (N - fw[N - pi]) - (pi + i)
        D[i] = min(D[i], mn)
        fw[N + 1 - pi] = N - (pi + i)

    print(*D)


solve()
