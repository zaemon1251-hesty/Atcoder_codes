from collections import deque


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
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]
    d = deque([])
    ans = []
    for q in queries:
        if q[0] == 1:
            x, c = q[1:]
            d.append((x, c))
        else:
            c = q[1]
            tr = 0
            ax = 0
            while d and tr < c:
                jx, jc = d.popleft()
                if tr + jc > c:
                    d.appendleft((jx, tr + jc - c))
                    jc = c - tr
                tr += jc
                ax += jx * jc
            ans.append(ax)
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
