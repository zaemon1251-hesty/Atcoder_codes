class Fenwick_Tree:
    def __init__(self, n):
        self._n = n
        self.data = [0] * n

    def add(self, p, x):
        assert 0 <= p < self._n
        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p

    def sum(self, l, r):
        assert 0 <= l <= r <= self._n
        return self._sum(r) - self._sum(l)

    def _sum(self, r):
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r
        return s


N = int(input())
S = [ord(x) - ord("a") for x in input()]  # アルファベット番号で受け取る
Q = int(input())
cmp = Fenwick_Tree(N)  # ソート済かを判定する、idxiとi+1の間がソート済でなければcmp[i]に1が立つ
cnt = [Fenwick_Tree(N) for _ in range(26)]  # それぞれのアルファベットについての位置
for i in range(N):
    cnt[S[i]].add(i, 1)
for i in range(N - 1):
    if S[i] > S[i + 1]:
        cmp.add(i, 1)


def update(i, x):
    """
    cntやcmpに対して
    場所iに関するデータをxだけ増やす(x=1なら増やす、-1なら減らす)
    """
    cnt[S[i]].add(i, x)
    if i >= 1 and S[i - 1] > S[i]:
        cmp.add(i - 1, x)
    if i + 1 < N and S[i] > S[i + 1]:
        cmp.add(i, x)


for qi in range(Q):
    q = input().split()
    if q[0] == "1":
        i = int(q[1])
        i -= 1
        c = ord(q[2]) - ord("a")
        # x文字目をcに置き換える
        update(i, -1)
        S[i] = c
        update(i, 1)
    else:
        l = int(q[1])
        l -= 1
        r = int(q[2])
        # 半開区間[l,r)にした
        ok = True
        if cmp.sum(l, r - 1):
            ok = False
        for char in range(S[l] + 1, S[r - 1]):
            if cnt[char].sum(l, r) != cnt[char].sum(0, N):
                ok = False
        if ok:
            print("Yes")
        else:
            print("No")
