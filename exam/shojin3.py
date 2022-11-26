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


def agc058_a():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N = ii()
    P = li()

    cnt = 0
    history = []
    for i in range(0, 2 * N - 1, 2):
        if P[i] > P[i + 1]:
            cnt += 1
            history.append(i + 1)
            P[i], P[i + 1] = P[i + 1], P[i]
    for i in range(1, 2 * N - 1, 2):
        if P[i] < P[i + 1]:
            cnt += 1
            history.append(i + 1)
            P[i], P[i + 1] = P[i + 1], P[i]
    print(cnt)
    print(*history)


def nikkei2019_qual_c():

    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N = ii()
    S = [li() + [i] for i in range(N)]
    S.sort(key=lambda x: (x[0] + x[1], -x[0]))

    s = 0
    i = 1
    while S:
        s += i * S.pop()[i - 1]
        i *= -1
    print(s)


def abc124_d():
    from itertools import groupby

    def runLengthEncode(S: str):
        # ランレングス符号化
        grouped = groupby(S)
        res = []
        for k, v in grouped:
            res.append((k, int(len(list(v)))))
        return res

    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N, K = mi()
    S = runLengthEncode(input())
    M = len(S)
    S.append(('X', 1))
    ans = 0
    R = 0
    cur = 0
    res = 0
    for L in range(M):
        while R < M and (cur < K or S[R][0] == "1"):
            res += S[R][1]
            if S[R][0] == "0":
                cur += 1
            ans = max(res, ans)
            R += 1

        res -= S[L][1]
        if S[L][0] == "0":
            cur -= 1
    print(ans)


def agc034_b():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    s = input().replace("BC", "D")
    cur_a = 0
    ans = 0
    for w in s:
        if w == "A":
            cur_a += 1
        elif w == "D":
            ans += cur_a
        else:
            cur_a = 0
    print(ans)


def arc111_a():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N, M = mi()
    a = pow(10, N, M**2)

    for r in range(M):
        if r * M <= a < (r + 1) * M:
            print(r)
            exit()


def diverta2019_d():
    def make_divisors(n):
        lower_divisors, upper_divisors = [], []
        i = 1
        while i * i <= n:
            if n % i == 0:
                lower_divisors.append(i)
                if i != n // i:
                    upper_divisors.append(n // i)
            i += 1
        return lower_divisors + upper_divisors[::-1]

    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N = ii()
    ans = 0
    for d in make_divisors(N)[1:]:
        m = d - 1
        if N // m == N % m:
            ans += m
    print(ans)


def arc084_a():
    from bisect import bisect_left, bisect_right

    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N = ii()
    A = sorted(li())
    B = sorted(li())
    C = sorted(li())

    ans = 0
    for i, b in enumerate(B):
        c_l = N - bisect_right(C, b)
        a_l = bisect_left(A, b)
        ans += c_l * a_l
    print(ans)


def arc118_c():
    N = int(input())
    cards = [6, 15, 10]

    for i in range(16, 10001):
        if len(cards) == N:
            break
        if any(i % card == 0 for card in [6, 15, 10]):
            cards.append(i)

    print(*cards)


def abc112_c():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N = ii()
    S = [li() for _ in range(N)]

    def height(x, y, cx, cy, h):
        return max(h - abs(x - cx) - abs(y - cy), 0)

    def check(h_, cx, cy):
        return all(
            height(s[0], s[1], cx, cy, h_) >= s[2]
            for s in S
        )

    for cx in range(101):
        for cy in range(101):
            ok = 10**12
            ng = -1
            while ok - ng > 1:
                cen = (ok + ng) // 2
                if check(cen, cx, cy):
                    ok = cen
                else:
                    ng = cen
            if all(
                height(s[0], s[1], cx, cy, ok) == s[2]
                for s in S
            ):
                print(cx, cy, ok)
                exit()
    print(-1)


def agc033_a():
    from collections import deque
    from math import inf

    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]

    H, W = mi()
    A = [input() for _ in range(H)]
    true_ans = 0
    ans = [[inf] * W for _ in range(H)]
    todos = [(i, j, 0) for i in range(H) for j in range(W) if A[i][j] == "#"]
    for t in todos:
        todo = deque([(t[0], t[1], 0)])
        while todo:
            x, y, t = todo.popleft()
            if ans[x][y] < t:
                continue
            ans[x][y] = t
            true_ans = max(true_ans, t)

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                # 0-indexで考える
                if nx < 0 or nx >= H or ny < 0 or ny >= W:
                    continue
                if A[nx][ny] == '#':
                    continue
                if ans[nx][ny] < t + 1:
                    continue
                todo.append((nx, ny, t + 1))
    print(true_ans)


def arc121_b():
    import sys
    readline = sys.stdin.readline

    N = int(readline())
    R, G, B = [], [], []
    for _ in range(2 * N):
        a, c = readline().rstrip().split()
        a = int(a)
        if c == 'R':
            R.append(a)
        if c == 'B':
            B.append(a)
        if c == 'G':
            G.append(a)
    r, g, b = len(R) % 2, len(G) % 2, len(B) % 2
    if r == g == b == 0:
        ans = 0
    else:
        def f(A, B):
            if not A or not B:
                return float('inf')
            a = len(A)
            b = len(B)
            i = 0
            j = 0
            ans = abs(A[0] - B[0])
            while i != a - 1 or j != b - 1:
                if i == a - 1:
                    j += 1
                elif j == b - 1:
                    i += 1
                else:
                    if A[i] < B[j]:
                        i += 1
                    else:
                        j += 1
                ans = min(ans, abs(A[i] - B[j]))
            return ans
        if r == 0:
            R, B = B, R
        elif g == 0:
            B, G = G, B
        R.sort()
        G.sort()
        B.sort()
        r = len(R)
        g = len(G)
        b = len(B)
        ans = min(f(R, G), f(R, B) + f(B, G))
    print(ans)


def tenka1_2017_c():
    from itertools import product

    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N = ii()
    for h, w in product(range(1, 3501), repeat=2):
        a = 4 * h * w - N * (h + w)
        b = N * h * w
        if a > 0 and b % a == 0:
            print(h, b // a, w)
            return


def arc109_c():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    n, k = mi()
    s = input()
    s = s

    battles = {
        ("R", "P"): "P",
        ("P", "R"): "P",
        ("P", "P"): "P",
        ("S", "P"): "S",
        ("P", "S"): "S",
        ("S", "S"): "S",
        ("R", "S"): "R",
        ("S", "R"): "R",
        ("R", "R"): "R"
    }

    for _ in range(k):
        ss = s + s
        t = []
        for i in range(len(ss) // 2):
            t.append(battles[ss[2 * i], ss[2 * i + 1]])
        s = t
    print(s[0])


def tenka1_2018_c():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N = ii()
    A = [ii() for _ in range(N)]
    i = 0
    f = 1
    coef, coef2 = [], []
    while i < N:
        if i == 0:
            coef.append((f, i))
            coef2.append((-f, i))
        elif i == N - 1:
            coef.append((f, i))
            coef2.append((-f, i))
        else:
            coef.append((2 * f, i))
            coef2.append((-2 * f, i))
        i += 1
        f *= -1
    ans = [-1] * N
    ans2 = [-1] * N

    coef.sort(key=lambda x: x[0])
    coef2.sort(key=lambda x: x[0])
    A.sort()

    for a, (_, i) in zip(A, coef):
        ans[i] = a
    solve1 = sum(abs(ans[i + 1] - ans[i]) for i in range(N - 1))

    for a, (_, i) in zip(A, coef2):
        ans2[i] = a
    solve2 = sum(abs(ans2[i + 1] - ans2[i]) for i in range(N - 1))

    print(max(solve1, solve2))


def arc081_b():

    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N = ii()
    S = [input(), input()]
    prev = -1
    MOD = 10**9 + 7
    loc = 0

    while loc < N:
        if S[0][loc] == S[1][loc]:
            if prev < 0:
                ans = 3
            elif prev == 0:
                ans *= 2
            else:
                ans *= 1

            prev = 0
            loc += 1
        else:
            if prev < 0:
                ans = 6
            elif prev == 0:
                ans *= 2
            else:
                ans *= 3

            prev = 1
            loc += 2

        ans %= MOD

    print(ans)


def abc121_d():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    A, B = mi()

    def f_get(i: int):
        """return reduce(xor, [0, 1, ..., i])

        Args:
            i (int):

        Returns:
            int:
        """
        if i % 2 == 0:
            if i % 4 == 0:
                return i

            return 1 ^ i

        if i % 4 == 1:
            return 1

        return 0

    if A == 0:
        print(f_get(B))
    else:
        print(f_get(A - 1) ^ f_get(B))


def abc048_c():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N, x = mi()
    A = li()

    def check():
        res = 0
        for i in range(N - 1):
            if A[i + 1] + A[i] > x:
                need = A[i + 1] + A[i] - x
                if A[i + 1] < need:
                    ai_need = need - A[i + 1]
                    A[i + 1] = 0
                    A[i] -= ai_need
                else:
                    A[i + 1] -= need

                res += need
        return res

    print(check())


if __name__ == '__main__':
    abc048_c()
