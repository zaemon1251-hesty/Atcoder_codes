class SegmentTree:
    def __init__(self, n, op, e):
        self.n = n
        self.op = op
        self.e = e
        self.size = 2 ** (n - 1).bit_length()
        self.data = [e] * (self.size * 2)

    def __repr__(self):
        l = self.size
        r = l + self.n
        res = ", ".join(map(str, self.data[l:r]))
        return f"SegmentTree([{res}])"

    def update(self, i):
        self.data[i] = self.op(self.data[i * 2], self.data[i * 2 + 1])

    def build(self, a):
        self.data[self.size : self.size + self.n] = a
        for i in range(self.size - 1, 0, -1):
            self.update(i)

    def set(self, p, x):
        p += self.size
        self.data[p] = x
        while p:
            p //= 2
            self.update(p)

    __setitem__ = set

    def get(self, p):
        return self.data[p + self.size]

    __getitem__ = get

    def prod(self, l, r):
        l += self.size
        r += self.size
        vl = vr = self.e
        while l < r:
            if l % 2:
                vl = self.op(vl, self.data[l])
                l += 1
            if r % 2:
                r -= 1
                vr = self.op(self.data[r], vr)
            l //= 2
            r //= 2
        return self.op(vl, vr)


def f():
    return map(int, input().split())


n = int(input())
E = []
G = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, w = f()
    u -= 1
    v -= 1
    E += [(u, v)]
    G[u] += [(v, w)]
    G[v] += [(u, w)]
I = [-1] * n
O = [-1] * n
P = [-1] * n
V = []
W = []
t = 0
Q = [(0, 0)]
while Q:
    v, w = Q.pop()
    if v >= 0:
        I[v] = t
        t += 1
        V += [v]
        if t > 1:
            W += [w]
        for c, w in G[v][::-1]:
            if c != P[v]:
                P[c] = v
                Q += [(~c, -w), (c, w)]
    else:
        v = ~v
        O[v] = t
        t += 1
        V += [P[v]]
        W += [w]
O[0] = t
STV = SegmentTree(n * 2 - 1, min, 4e5)
STV.build([I[v] for v in V])


def op(x, y):
    return x + y


STW = SegmentTree(n * 2 - 2, op, 0)
STW.build(W)
q = int(input())
for _ in range(q):
    t, *Q = f()
    if t == 1:
        i, w = Q
        p, v = E[i - 1]
        if p != P[v]:
            p, v = v, p
        STW[I[v] - 1] = w
        STW[O[v] - 1] = -w
    if t == 2:
        u, v = Q
        u -= 1
        v -= 1
        if I[u] > I[v]:
            u, v = v, u
        a = V[STV.prod(I[u], I[v] + 1)]
        wau = STW.prod(I[a], I[u])
        wav = STW.prod(I[a], I[v])
        print(wau + wav)
