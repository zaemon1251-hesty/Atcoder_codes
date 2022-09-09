class Fenwick:
    def __init__(self, n):
        self.n = n
        self.n0 = 2**(n - 1).bit_length()
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


# これはXor演算
n, q = map(int, input().split())
a = list(map(int, input().split()))
bit = [0] * (n + 1)


def add(i, x):
    i += 1
    while i <= n:
        bit[i] ^= x
        i += i & -i


def get(l, r):
    # [l+1,r]の区間で演算される
    res = 0
    while l:
        res ^= bit[l]
        l -= l & -l
    while r:
        res ^= bit[r]
        r -= r & -r
    return res


for i in range(n):
    add(i, a[i])

for _ in range(q):
    t, x, y = map(int, input().split())
    if t == 1:
        add(x - 1, y)
    else:
        print(get(x - 1, y))
