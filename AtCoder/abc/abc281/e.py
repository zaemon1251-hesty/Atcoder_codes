from bisect import bisect_left
import sys
input = sys.stdin.readline


class Compress:
    def __init__(self, vs):
        self.xs = list(set(vs))
        self.xs.sort()

    def compress(self, x):
        return bisect_left(self.xs, x)

    def decompress(self, i):
        return self.xs[i]

    def size(self):
        return len(self.xs)


class FenwickTree:
    def __init__(self, size):
        self.data = [0] * (size + 1)
        self.size = size

    # i is exclusive
    def prefix_sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.data[i] += x
            i += i & -i

    def lower_bound(self, x):
        if x <= 0:
            return 0
        k = 1
        while k * 2 <= self.size:
            k *= 2
        i = 0
        while k > 0:
            if i + k <= self.size and self.data[i + k] < x:
                x -= self.data[i + k]
                i += k
            k //= 2
        return i


N, M, K = map(int, input().split())
A = list(map(int, input().split()))
comp = Compress(A)
B = [comp.compress(x) for x in A]
ft_cnt = FenwickTree(comp.size())
ft_sum = FenwickTree(comp.size())
for i in range(M):
    ft_cnt.add(B[i], 1)
    ft_sum.add(B[i], A[i])
ans = []
for i in range(N - M + 1):
    x = ft_cnt.lower_bound(K)
    ans.append(
        ft_sum.prefix_sum(x) - comp.decompress(x) * (ft_cnt.prefix_sum(x) - K)
    )

    ft_cnt.add(B[i], -1)
    ft_sum.add(B[i], -A[i])
    if i + M < N:
        ft_cnt.add(B[i + M], 1)
        ft_sum.add(B[i + M], A[i + M])
print(*ans)
