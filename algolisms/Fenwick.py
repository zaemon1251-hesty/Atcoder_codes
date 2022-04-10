
class BIT:
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

    def get(self, l, r) -> int:
        # [l+1,r]の区間で演算される
        res = self.ele
        while l:
            res = self.func(res, self.bit[l])
            l -= l & -l
        while r:
            res = self.func(res, self.bit[r])
            r -= r & -r
        return res

    def sum(self, i):
        # [0, i] での演算
        i += 1
        res = self.ele
        while i > 0:
            res = self.func(res, self.bit[i])
            i -= i & -i
        return res


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
