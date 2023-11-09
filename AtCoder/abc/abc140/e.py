# method.1
# BIT + Sigma Pi(for 1 to N) x Ci(範囲組合せ)
# Pi = X_L,R になる (L,R)の組
# Ci : Piが成り立つ範囲の組合せ


class BIT:
    def __init__(self, n):
        self.n = n
        self.LV = (n - 1).bit_length()
        self.base_idx = 2**self.LV
        self.data = [0] * (n + 1)  # 1-indexed
        # self.el = [0]*(n+1) # getをO(1)に高速化したい場合。SegmentTreeでいいんじゃない？

    def init(self, al):
        self.data[1:] = al
        for i in range(1, self.n):
            if i + (i & -i) <= self.n:
                self.data[i + (i & -i)] += self.data[i]
                # (i & -i) : 右から見て最初の'1'を抽出 5(101b)+1(001b)-> 6
                # (i & -i) : 右から見て最初の'1'を抽出 12(1100b)+4(100b)-> 16(10000b)
                # ex.6(110b): data[110b] = data[5:5(101b)] + {data[6:6(110b)]}
                # ex.16(10000b): data[10000b] =
                # data[1:8(1000b)]+data[9:12(1100b)]+data[13:14(1110b)]+data[15:15(1111b)+{data[16:16]]}

    def sum(self, i):  # i以下の要素数、i以下の総和でもあるけど
        ans = 0
        while i > 0:
            ans += self.data[i]
            i -= i & -i
        return ans

    def add(self, i, x=1):  # ★ i > 0
        while i <= self.n:
            self.data[i] += x
            i += i & -i
            # i == 5  101b+1b → 110b+10b → 1000b

    def get(self, l, r=None):
        if r:
            return self.sum(r) - self.sum(l)
        return self.sum(l) - self.sum(l - 1)
        # if self.el(l): return self.el(l) getをO(1)にする場合

    def lower_bound(self, w):  # 小さい方から w 番目の要素
        x = 0
        k = self.base_idx
        while k > 0:
            if x + k <= self.n and self.data[x + k] <= w:
                w -= self.data[x + k]
                x += k
            k >>= 1
        return x

    def lower_bound2(self, w):  # 小さい方から w 番目の要素 範囲外: min,0 max n+1
        ng = -1
        ok = self.n + 1
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if self.sum(mid) >= w:
                ok = mid
            else:
                ng = mid
        return ok


N = int(input())
P = list(map(int, input().split()))
pl = [0] * (N + 1)
for i in range(N):
    pl[P[i]] = i + 1
ans = 0
bit = BIT(N)
for i in range(N, 0, -1):
    pidx = pl[i]
    bit.add(pidx)
    cnt = bit.sum(pidx)
    a = bit.lower_bound2(cnt - 2)
    b = bit.lower_bound2(cnt - 1)
    c = bit.lower_bound2(cnt + 1)
    d = bit.lower_bound2(cnt + 2)
    if b != 0:
        ans += (b - a) * (c - pidx) * i
    if c != N + 1:
        ans += (d - c) * (pidx - b) * i
print(ans)
