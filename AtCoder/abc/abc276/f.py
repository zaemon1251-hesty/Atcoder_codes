import sys


MOD = 998244353


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


def input():
    return sys.stdin.readline().rstrip()


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    _ = ii()
    A = li()

    M = max(A)

    bit = Fenwick(M)
    bit_v = Fenwick(M)

    ans = 0

    for k, a in enumerate(A):
        ans = ans + 2 * (a * bit.sum(a) + bit_v.sum(M) - bit_v.sum(a)) + a
        ans %= MOD
        div = pow((k + 1) ** 2, MOD - 2, MOD)

        print(ans * div % MOD)

        bit.add(a, 1)
        bit_v.add(a, a)


if __name__ == "__main__":
    main()
