from collections import defaultdict


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


################################


if __name__ == "__main__":
    n = int(input())
    COLORS = defaultdict(list)
    Q = zip(map(int, input().split()), map(int, input().split()))
    Q = list(Q)

    for i, (c, x) in enumerate(Q):
        COLORS[0].append(x)
        COLORS[c].append(x)

    fw = Fenwick(n)
    ans = 0
    for c, cols in COLORS.items():
        for j, x in enumerate(cols):
            fw.add(x, 1)
            operand = j + 1 - fw.sum(x)
            if c == 0:
                ans += operand
            else:
                ans -= operand
        for x in cols:
            fw.add(x, -1)
    print(ans)
