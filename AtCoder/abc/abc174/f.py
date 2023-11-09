class BIT:
    """
    Binary Indexed Tree
    演算は足し算
    """

    def __init__(self, n, func, ele) -> None:
        self.n = n
        self.ele = ele
        self.func = func
        self.bit = [ele] * (n + 1)

    def add(self, i, x) -> None:
        while i <= self.n:
            self.bit[i] = self.func(self.bit[i], x)
            i += i & -i

    def sum(self, i):
        # [0, i] での演算
        res = self.ele
        while i > 0:
            res = self.func(res, self.bit[i])
            i -= i & -i
        return res


N, Q = map(int, input().split())
C = [0] + list(map(int, input().split()))
col = [0] * (N + 1)
cnum = BIT(N, lambda x, y: x + y, 0)
ql = [[] for _ in range(N + 1)]
pos = [[] for _ in range(N + 1)]
for i in range(Q):
    l, r = map(int, input().split())
    ql[r].append(l)
    pos[r].append(i)
ans = [0] * Q

for r in range(1, N + 1):
    # cnum は 1-indexed
    if col[C[r]] > 0:
        cnum.add(col[C[r]], -1)
    cnum.add(r, 1)
    col[C[r]] = r
    for l in range(len(pos[r])):
        ans[pos[r][l]] = cnum.sum(r) - cnum.sum(ql[r][l] - 1)

print(*ans, sep="\n")
