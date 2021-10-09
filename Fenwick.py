
class BIT:
    """
    Binary Indexed Tree
    演算は足し算
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


# これはXor演算
n, q = map(int, input().split())
a = list(map(int, input().split()))
bit = [0]*(n+1)


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
        add(x-1, y)
    else:
        print(get(x-1, y))
