from bisect import bisect_left
from itertools import product
import sys


def input():
    return sys.stdin.readline().rstrip()


def gridint(s):
    return 0 if s == "." else 1


class Fenwick:
    def __init__(self, n):
        self.n = n
        self.n0 = 2 ** (n - 1).bit_length()
        self.data = [0] * (n + 1)
        self.el = [0] * (n + 1)

    def init(self, A):
        self.data[1:] = A
        for i in range(1, self.n):
            if i + (i & -i) <= self.n:
                self.data[i + (i & -i)] += self.data[i]

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def add(self, i, x):
        # assert i > 0
        self.el[i] += x
        while i <= self.n:
            self.data[i] += x
            i += i & -i

    def get(self, i, j=None):
        if j is None:
            return self.el[i]
        return self.sum(j) - self.sum(i)

    def lower_bound(self, x):
        """returns i = &t = min({t | t > x})"""
        w = i = 0
        k = self.n0
        while k:
            if i + k <= self.n and w + self.data[i + k] <= x:
                w += self.data[i + k]
                i += k
            k >>= 1
        # assert self.get(0, i) <= x < self.get(0, i+1)
        return i + 1


def main():
    ans = 0

    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    H, W = mi()
    S = [list(map(gridint, input())) for _ in range(H)]
    rowobj = [[-1] for _ in range(H)]
    colobj = [[-1] for _ in range(W)]

    for i, j in product(range(H), range(W)):
        if S[i][j] == 1:
            rowobj[i].append(j)
            colobj[j].append(i)

    for i in range(H):
        rowobj[i].append(W)
    for j in range(W):
        colobj[j].append(H)

    for i, j in product(range(H), range(W)):
        if S[i][j] == 1:
            continue

        obsth_i = bisect_left(rowobj[i], j)
        obsth_i %= len(rowobj[i])
        L = j - rowobj[i][obsth_i - 1] - 1
        R = rowobj[i][obsth_i] - j - 1

        obstw_i = bisect_left(colobj[j], i)
        obstw_i %= len(colobj[j])

        D = i - colobj[j][obstw_i - 1] - 1
        U = colobj[j][obstw_i] - i - 1

        ans = max(L + R + U + D + 1, ans)

    print(ans)


if __name__ == "__main__":
    main()
