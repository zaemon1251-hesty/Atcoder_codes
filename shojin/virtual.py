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


def arc045_b():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N, M = mi()

    covers = [li() for _ in range(M)]

    fw_ext = Fenwick(N + 1)
    fw_cnt = Fenwick(N + 1)

    classes_cnt = [0] * (N + 1)

    for i in range(M):
        x, y = covers[i]
        classes_cnt[x - 1] += 1
        classes_cnt[y] -= 1

    for i in range(N):
        classes_cnt[i + 1] += classes_cnt[i]

    classes_ext = [classes_cnt[i] > 0 for i in range(N)]

    fw_ext.init(classes_ext)
    fw_cnt.init(classes_cnt)

    ans = []
    for ex_i in range(M):
        x, y = covers[ex_i]
        fw_cnt.add(x - 1, -1)
        fw_cnt.add(y, 1)

        # TODO fw_ext.update(x-1, y) を効率的に実装する

        if fw_ext.get(1, N) < N:
            ans.append(ex_i + 1)

    print(len(ans))
    if len(ans) > 0:
        print(*ans, sep="\n")


def abc032_c():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N, K = mi()
    s = [ii() for _ in range(N)]
    if 0 in s:
        print(N)
        return

    def interval(A, K):
        # 尺取り法
        # 和がKとなる区間のうち最大の長さを求める
        ans = 0
        N = len(A)
        _sum = 1
        right = 0
        for left in range(N):
            while right < N and _sum * A[right] <= K:
                _sum *= A[right]
                ans = max(ans, right - left + 1)
                right += 1
            if left == right:
                right += 1
            if _sum % A[left] == 0:
                _sum //= A[left]
        return ans

    print(interval(s, K))


if __name__ == "__main__":
    abc032_c()
