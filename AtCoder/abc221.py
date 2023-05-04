from collections import defaultdict
from typing import OrderedDict


def maina():
    a, b = map(int, input().split())
    print(pow(32, a-b))


def mainb():
    s = input()
    t = input()
    cnt = []
    for i in range(len(s)):
        if s[i] != t[i]:
            cnt.append((s[i], t[i], i))
    if len(cnt) == 2:
        a, b = cnt[0], cnt[1]
        if a[0] == b[1] and a[1] == b[0] and abs(a[2]-b[2]) == 1:
            cnt = []
    print("Yes" if len(cnt) == 0 else "No")


def mainc():
    t = list(input())
    N = len(t)
    ans = 0
    for i in range(1 << N):
        a = []
        b = []
        for j in range(N):
            if (i >> j) & 1:
                a.append(int(t[j]))
            else:
                b.append(int(t[j]))
        a = "".join(list(map(str, sorted(a, reverse=True))))
        b = "".join(list(map(str, sorted(b, reverse=True))))
        #print(a, b)
        if a == "" or b == "":
            continue
        ans = max(ans, int(a) * int(b))
    print(ans)


mainc()


def mainc():
    A = list(input())
    N = len(A)
    ans = -1 << 18
    for i in range(1 << N):
        x = []
        y = []
        for j in range(N):
            if (i >> j) & 1:
                x.append(A[j])
            else:
                y.append(A[j])
        try:
            x = sorted(x, reverse=True)
            y = sorted(y, reverse=True)
            x = int(''.join(x))
            y = int(''.join(y))
        except:
            x, y = 0, 0
        ans = max(ans, x*y)
    print(ans)


def maind():
    """
    座標圧縮 & imos
    """
    from collections import defaultdict
    N = int(input())
    T = []
    Event = defaultdict(int)
    Event[0] = 0
    Event[pow(10, 100)] = 0
    for _ in range(N):
        t = list(map(int, input().split()))
        Event[t[0]] += 1
        Event[t[0] + t[1]] += -1
        T.append(t)

    T.sort(key=lambda arr: arr[0])
    Event = sorted(Event.items(), key=lambda x: x[0])
    ans = [0]*N
    for i in range(len(Event)):
        if i == len(Event)-1:
            continue
        Event[i] = list(Event[i])
        Event[i][1] += Event[i-1][1]
        num = Event[i][1]-1
        if num >= 0:
            ans[num] += Event[i+1][0] - Event[i][0]

    print(*ans, sep=" ")


def maine():
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


class BIT:
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


if __name__ == "__main__":
    pass
    # maine()
