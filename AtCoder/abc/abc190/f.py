# Binary Indexed Tree (Fenwick Tree)
# 1-index のインターフェース


class Fenwick:
    def __init__(self, n):
        self.n = n
        self.n0 = 2 ** (n - 1).bit_length()
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


def main():
    N = int(input())
    A = list(map(int, input().split()))
    bt = Fenwick(N)
    ans = 0
    for i in range(N):
        tmp = bt.get(A[i] + 1, N)
        ans += tmp
        bt.add(A[i] + 1, 1)
    for i in range(N):
        print(ans)
        ans += N - 1 - A[i]
        ans -= A[i]


if __name__ == "__main__":
    main()
