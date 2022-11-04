from math import inf
import sys
from itertools import product, combinations


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r))
                         for r in self.roots())


def input():
    return sys.stdin.readline().rstrip()


def arc023_2():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    R, C, D = mi()
    A = [li() for _ in range(R)]
    ans = -inf
    for x, y in product(range(R), range(C)):
        fst = x + y
        if fst <= D and fst % 2 == D % 2:
            ans = max(ans, A[x][y])
    print(ans)


def arc036_b():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N = ii()
    H = [ii() for _ in range(N)]

    if N == 1:
        print(1)
        exit()

    mounts = []
    mount = [0, -1, -1]
    for i in range(N - 1):
        if mount[0] == 0 and H[i + 1] > H[i]:
            mount[0] = 1
            mount[1] = i
        elif mount[0] == 0 and H[i + 1] < H[i]:
            mount[0] = -1
            mount[1] = i
        elif mount[0] == 1 and H[i + 1] > H[i]:
            pass
        elif mount[0] == 1 and H[i + 1] < H[i]:
            mount[0] = -1
        elif mount[0] == -1 and H[i + 1] < H[i]:
            pass
        elif mount[0] == -1 and H[i + 1] > H[i]:
            mount[2] = i
            mounts.append(mount)
            mount = [1, i, -1]

    mount[2] = N - 1
    mounts.append(mount)

    print(max(u - s + 1 for _, s, u in mounts))


def arc037_b():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N, M = mi()
    bad_roots = set()
    uf = UnionFind(N)
    for _ in range(M):
        u, v = mi()
        u -= 1
        v -= 1
        if uf.same(u, v):
            bad_roots.add(uf.find(u))
        uf.union(u, v)

    print(sum((uf.parents[i] < 0 and i not in bad_roots) for i in range(N)))


def arc097_a():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    s = input()
    N = len(s)
    K = ii()
    ans_set = set()
    for i, j in combinations(range(N + 1), 2):
        if j - i >= 6:
            continue
        ans_set.add(s[i:j])
    ans_set = sorted(ans_set)
    print(ans_set[K - 1])


def caddi2018_b():
    N = int(input())
    a = [int(input()) for _ in range(N)]
    print('second' if all(a[i] % 2 == 0 for i in range(N)) else 'first')


def panasonic2020_d():
    import sys
    sys.setrecursionlimit(10**6)

    N = int(input())
    base = ord("a")
    buf = ["a"]
    ans = []

    def dfs(max_code):
        if len(buf) == N:
            ans.append("".join(buf))
            return
        for c in range(base, max_code + 2):
            buf.append(chr(c))
            dfs(max(c, max_code))
            buf.pop()

    dfs(base)

    print(*ans, sep="\n")


def arc091_b():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N, K = mi()
    ans = 0

    if K == 0:
        print(N * N)
        exit()

    for b in range(K + 1, N + 1):
        k = 0
        while k * b + K <= N:
            ans += min(k * b + b - 1, N) - (k * b + K) + 1
            k += 1
    print(ans)


def abc099_c():
    import sys
    from functools import lru_cache
    sys.setrecursionlimit(10**6)

    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N = ii()

    @lru_cache(None)
    def dfs(k: int) -> int:
        if k == 0:
            return 0

        res = k
        a, b = 6, 9

        while a <= k:
            res = min(res, dfs(k - a) + 1)
            a *= 6

        while b <= k:
            res = min(res, dfs(k - b) + 1)
            b *= 9

        return res

    s = dfs(N)
    print(s)


def abc080_c():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N = ii()
    F = [li() for _ in range(N)]

    P = [li() for _ in range(N)]

    ans = -inf
    for s in range(1 << 10):
        if s == 0:
            continue
        joisino = [0] * 10
        for i in range(10):
            if s >> i & 1:
                joisino[i] = 1

        res = 0
        for shop_i in range(N):
            with_cnt = sum(
                joisino_on * shop_on
                for joisino_on, shop_on
                in zip(joisino, F[shop_i])
            )
            res += P[shop_i][with_cnt]

        ans = max(ans, res)

    print(ans)


if __name__ == '__main__':
    abc080_c()
