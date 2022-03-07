# Binary Indexed Tree (Fenwick Tree)
# 1-index のインターフェース
class BIT:
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


Q = int(input())
L = [list(map(int, input().split())) for _ in range(Q)]
S = set()
for i in range(Q):
    S.add(L[i][1])
x_to_i = {x: i for i, x in enumerate(sorted(S), 1)}
i_to_x = {i: x for i, x in enumerate(sorted(S), 1)}
N = len(S)
bit = BIT(N)
ans = []
for i in range(Q):
    if L[i][0] == 1:
        bit.add(x_to_i[L[i][1]], 1)
    elif L[i][0] == 2:
        x, k = L[i][1], L[i][2]
        tmp = bit.sum(x_to_i[x])
        if tmp < k:
            ans.append(-1)
        else:
            # print("tmp:%s, tg:%s, lb:%s, i_to_x:%s" % (
            #     tmp,
            #     tmp - k,
            #     bit.lower_bound(tmp - k),
            #     i_to_x[bit.lower_bound(tmp - k)]
            # ))
            ans.append(i_to_x[bit.lower_bound(tmp - k)])
    else:
        x, k = L[i][1], L[i][2]
        total = bit.sum(N)
        l = 0
        if x_to_i[x] != 1:
            l = bit.sum(x_to_i[x] - 1)
        if total - l < k:
            ans.append(-1)
        else:
            # print("l:%s, tg:%s, lb:%s, i_to_x:%s" % (
            #     l,
            #     l + k - 1,
            #     bit.lower_bound(l + k - 1),
            #     i_to_x[bit.lower_bound(l + k - 1)]
            # ))
            ans.append(i_to_x[bit.lower_bound(l + k - 1)])

print(*ans, sep="\n")
