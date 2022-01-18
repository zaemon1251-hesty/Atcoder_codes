from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A = list(enumerate(A))
A.sort(key=lambda x: (x[1], -B[x[0]]))
compress(B)
fwc = BIT(N, lambda x, y: x + y, 0)
ans = 0
dub = defaultdict(int)
for i in range(N):
    idx = A[i][0]
    fwc.add(B[idx], 1)
    ans += dub[(A[i][1], B[idx])] + fwc.sum(B[idx], N)
    dub[(A[i][1], B[idx])] += 1
print(ans)
s UnionFind:
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
s BIT:
"""
Binary Indexed Tree
演算は足し算
"""
def __init__(self, n, func, ele) -> None:
    self.n = n
    self.ele = ele
    self.func = func
    self.bit = [ele]*(n+1)
def add(self, i, x) -> None:
    i += 1
    while i <= self.n:
        self.bit[i] = self.func(self.bit[i], x)
        i += i & -i
def sum(self, l, r):
    return self._sum(r) - self._sum(l)
def _sum(self, r):
    s = 0
    while r > 0:
        s += self.bit[r]
        r -= r & -r
    return s
compress(A):
res = list(enumerate(A))
res.sort(key=lambda x: x[1])
t = min(A) - 1
dst = -1
for ord in range(len(A)):
    i, a = res[ord]
    if t < a:
        t = a
        dst += 1
    A[i] = dst
return None
_name__ == '__main__':
mainf()
