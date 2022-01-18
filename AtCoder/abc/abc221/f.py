mod = 998244353
N = int(input())
A = list(map(int, input().split()))
w = enumerate(A)
w = sorted(w, key=lambda x: (x[1]))
rank = [0]*N
cnt = 0
pre = w[0][1]
for i, a in w:
    if pre != a:
        cnt += 1
    rank[i] = cnt
    pre = a
s = BIT(len(rank))
ans = 0
for i in range(N):
    ans += s.sum(rank[i])*pow(2, i, mod)
    ans %= mod
    s.add(rank[i], pow(2, mod-i-2, mod), mod)
print(ans)
s BIT:
"""
Binary Indexed Tree
"""
def __init__(self, n) -> None:
    self.n = n
    self.bit = [0]*(n+1)
def add(self, i, x, mod=1) -> None:
    i += 1
    while i <= self.n:
        self.bit[i] += x
        self.bit[i] %= mod
        i += i & -i
def get(self, l, r, mod=1) -> int:
    # [l+1,r]の区間で演算される
    res = 0
    while l:
        res += self.bit[l]
        l -= l & -l
    while r:
        res += self.bit[r]
        r -= r & -r
    return res % mod
def sum(self, i):
    i += 1
    s = 0
    while i > 0:
        s += self.bit[i]
        i -= i & -i
    return s
_name__ == "__main__":
pass
# maine()
