class Fenwick:
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


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    D = list(map(int, input().split()))
    wdt = enumerate(sorted(set(B) | set(D)), 1)
    x_to_i = {x: i for i, x in wdt}
    # i_to_x = {i: x for i, x in wdt}
    B = list(map(lambda x: x_to_i[x], B))
    D = list(map(lambda x: x_to_i[x], D))
    buf = list(zip([1] * M, C, D)) + list(zip([0] * N, A, B))
    buf.sort(key=lambda x: (x[1], x[0]))
    bt = Fenwick(N + M)
    while buf:
        q, _, w = buf.pop()
        if q == 1:
            bt.add(w, 1)

        elif q == 0:
            if bt.get(w - 1, bt.n) == 0:
                # (横幅) in [w, N+M] の箱が存在しないなら終了
                print("No")
                exit()

            # 二分探索で横幅が w 以上の箱のうち、最小の横幅のものを取得する
            # ちなみにwはインデックス
            ok = bt.n
            ng = w - 1
            while ok - ng > 1:
                mid = (ng + ok) // 2
                if bt.get(w - 1, mid) > 0:
                    ok = mid
                else:
                    ng = mid
            bt.add(ok, -1)
    print("Yes")


if __name__ == '__main__':
    main()
