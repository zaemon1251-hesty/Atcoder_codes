import sys


def input():
    return sys.stdin.readline().rstrip()


def arc074_a():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    H, W = mi()
    ans = 1 << 60
    for h in range(1, H + 1):
        b = h * W
        c2, d2 = ((H - h) // 2) * W, (H - h) * (W // 2)
        c3, d3 = H * W - b - c2, H * W - b - d2
        ans = min(ans, max(b, c2, c3) - min(b, c2, c3))
        ans = min(ans, max(b, d2, d3) - min(b, d2, d3))

    H, W = W, H
    for h in range(1, H + 1):
        b = h * W
        c2, d2 = ((H - h) // 2) * W, (H - h) * (W // 2)
        c3, d3 = H * W - b - c2, H * W - b - d2
        ans = min(ans, max(b, c2, c3) - min(b, c2, c3))
        ans = min(ans, max(b, d2, d3) - min(b, d2, d3))

    print(ans)


def abc089_d():
    from itertools import product

    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    H, W, D = mi()
    A = [li() for _ in range(H)]
    M = [[] for i in range(D)]
    for h, w in product(range(H), range(W)):
        M[A[h][w] % D].append((A[h][w], h, w))

    S = [[0] for i in range(D)]
    ref = {}
    for d in range(D):
        M[d].sort(key=lambda x: x[0])

        for i, (axy, x, y) in enumerate(M[d]):
            ref[axy] = i
            if i == len(M[d]) - 1:
                break
            _, u, v = M[d][i + 1]
            res = abs(x - u) + abs(y - v)
            S[d].append(S[d][-1] + res)

    Q = ii()
    que = [li() for _ in range(Q)]

    for s in range(Q):
        L, R = que[s]
        res = 0
        d = L % D
        src = ref[L]
        dst = ref[R]
        # print(M[d])
        # print(S[d])
        # print(d, src, dst)
        print(S[d][dst] - S[d][src])


def arc119_b():
    N = int(input())
    S = list(input())
    T = list(input())
    if S.count("1") != T.count("1"):
        print(-1)
        exit()

    z_s = [i for i in range(N) if S[i] == "0"]
    z_t = [i for i in range(N) if T[i] == "0"]

    print(sum(s != t for s, t in zip(z_s, z_t)))


def abc096_d():
    def get_prime(n, get_sieve=False):
        prime = [False] * 2 + [True] * (n - 2)
        for i in range(2, n):
            if prime[i]:
                for j in range(i * 2, n, i):
                    prime[j] = False
        if get_sieve:
            return [i for i in range(2, n) if prime[i]]
        else:
            return prime

    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N = ii()
    primes = get_prime(55555, True)
    primes = [i for i in primes if i % 5 == 1]
    print(*primes[:N])


def arc106_c():
    N, M = map(int, input().split())

    if M == 0:
        i = 1
        cnt = 0
        while cnt < N:
            print(i, i + 1)
            i += 2
            cnt += 1
        return

    elif M < 0 or M >= N - 1:
        print(-1)
        return

    else:
        i = 2
        cnt = 0
        while cnt < M + 1:
            print(i, i + 1)
            i += 2
            cnt += 1

        i += 2
        print(1, i)
        cnt += 1

        i += 1
        while cnt < N:
            print(i, i + 1)
            cnt += 1
            i += 2


def agc003_b():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    ans = 0

    breakpoints = set(i for i in range(N) if A[i] == 0)
    breakpoints.add(N)

    cur = 0
    for i in range(N + 1):
        if i in breakpoints:
            ans += cur // 2
            cur = 0
            continue
        cur += A[i]
    print(ans)


def abc070_d():
    import sys
    sys.setrecursionlimit(10**6)

    N = int(input())
    G = [[] for _ in range(N)]

    for _ in range(N - 1):
        a, b, c = map(int, input().split())
        a, b = a - 1, b - 1
        G[a].append((b, c))
        G[b].append((a, c))

    Q, K = map(int, input().split())
    K -= 1

    # Euler Tour Technique
    dist = [0] * N

    def dfs(v, p, d):
        for w, c in G[v]:
            if w == p:
                continue
            dist[w] = dist[v] + c
            dfs(w, v, d + 1)
    dist[K] == 0
    dfs(K, -1, 0)

    q = [list(map(int, input().split())) for _ in range(Q)]
    for x, y in q:
        x, y = x - 1, y - 1
        print(dist[x] + dist[y])


def agc014_b():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N, M = mi()
    E = [li() for _ in range(M)]
    cnt = [0] * N
    for a, b in E:
        cnt[a - 1] += 1
        cnt[b - 1] += 1

    if all(cn % 2 == 0 for cn in cnt):
        print("YES")
        return

    print("NO")


def nomura2020_c():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N = ii()
    A = li()
    if N == 0:
        print(1 if A[0] == 1 else -1)
        return
    if A[0] == 1:
        print(-1)
        return

    ub = []
    lb = []

    cur = 0
    for a in A[::-1]:
        cur += a
        lb.append(cur)
    lb.reverse()

    cur = 1
    ub.append(1)
    for a in A[1:]:
        cur *= 2
        ub.append(cur)
        if a > cur:
            print(-1)
            return
        cur -= a

    print(sum(min(uu, ll) for uu, ll in zip(ub, lb)))


def main():
    from functools import lru_cache

    @lru_cache(None)
    def f(x: int):
        if x == 1:
            return 3
        return 2 * f(x - 1) + 3

    @lru_cache(None)
    def find(lev, p):
        length = f(lev)
        cen = (length + 1) // 2
        if p == 1:
            return "A"
        elif p == length:
            return "C"
        elif p == cen:
            return "B"
        elif p < cen:
            return find(lev - 1, p - 1)
        else:
            return find(lev - 1, p - cen)

    k, s, t = map(int, input().split())

    ans = [find(k, i) for i in range(s, t + 1)]

    print(*ans, sep="")


class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    find_rightest(a, b, x): [a,b)区間のx以下となる一番右のインデックスを取り出す O(logN)
    find_leftest(a, b, x): [a,b)区間のx以下となる一番左のインデックスを取り出す O(logN)
    get region(i): iを含み、区間積が tree[num + i - 1] となる区間 [l, r) を取り出す O(logN)
    """

    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.n = n
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

    def find_rightest(self, a, b, x):
        """
        [a,b)区間のx以下となる一番右のインデックスを取り出す
        """
        return self.find_rightest_sub(a, b, x, 0, 0, self.n)

    def find_leftest(self, a, b, x):
        """
        [a,r)区間のx以下となる一番左のインデックスを取り出す
        """
        return self.find_leftest_sub(a, b, x, 0, 0, self.n)

    def find_rightest_sub(self, a, b, x, k, l, r):
        """
        find_ringtestのサブルーチン
        [参考サイト]
        https://algo-logic.info/segment-tree/
        """
        if self.tree[k] > x or r <= a or l >= b:
            return max(a - 1, 0)
        elif k >= self.num - 1:
            return k - self.n - 1
        else:
            vr = self.find_rightest_sub(a, b, x, 2 * k + 2, (l + r) // 2, r)
            if vr != a - 1:
                return vr
            else:
                return self.find_rightest_sub(
                    a, b, x, 2 * k + 1, l, (l + r) // 2)

    def find_leftest_sub(self, a, b, x, k, l, r):
        """
        find_leftestのサブルーチン
        [参考サイト]
        https://algo-logic.info/segment-tree/
        """
        if self.tree[k] > x or r <= a or l >= b:
            return min(b, self.n - 1)
        elif k >= self.num - 1:
            return k - self.n - 1
        else:
            vr = self.find_rightest_sub(a, b, x, 2 * k + 1, l, (r + l) // 2)
            if vr != b:
                return vr
            else:
                return self.find_rightest_sub(
                    a, b, x, 2 * k + 2, (l + r) // 2, r)


def sub():
    N, M = map(int, input().split())
    _ = [int(input()) for _ in range(N)]


def try_():
    from string import ascii_lowercase
    import sys
    sys.setrecursionlimit(10**6)
    s = input()
    n = len(s)
    digits = set([str(i) for i in range(10)])

    stack = []
    brackets = {}
    for i in range(n):
        if s[i] == "(":
            stack.append(i)
        elif s[i] == ")":
            st = stack.pop()
            brackets[st] = i

    def getInt(st: int, en: int) -> tuple[int, int]:
        assert s[st] in digits

        i = st
        while i < en and s[i] in digits:
            i += 1

        int_ = 1
        if i > st:
            int_ = int(s[st:i])

        return int_, i - 1

    def counting(t: str, st, en) -> int:
        res = 0
        i = st
        int_ = 1
        while i < en:
            if s[i] in digits:
                int_, i = getInt(i, en)
            elif s[i] == t:
                res += int_
                int_ = 1
            elif s[i] == "(":
                mid_en = brackets[i] - 1
                res += int_ * counting(t, i + 1, mid_en + 1)
                i = mid_en
            else:
                int_ = 1
            i += 1

        return res

    for a in ascii_lowercase:
        print(a, counting(a, 0, n))


def arc083_a():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    A, B, C, D, E, F = mi()
    ma = 0
    ans1 = 100 * A
    ans2 = 0
    dp = [[0] * (F + 10) for _ in range(F + 10)]
    dp[0][0] = 1
    for i in range(1, F + 1):
        for j in range(i + 1):
            if i >= 100 * A and dp[i - 100 * A][j] > 0:
                dp[i][j] = 1
            if i >= 100 * B and dp[i - 100 * B][j] > 0:
                dp[i][j] = 1
            if j >= C and dp[i - C][j - C] > 0:
                dp[i][j] = 1
            if j >= D and dp[i - D][j - D] > 0:
                dp[i][j] = 1

            if not dp[i][j]:
                continue

            if 100 * j <= E * (i - j) and j / i > ma:
                ma = j / i
                ans1 = i
                ans2 = j
    print(ans1, ans2)


def abc054_c():
    from itertools import permutations

    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N, M = mi()

    ans = 0
    G = [set() for _ in range(N)]
    for _ in range(M):
        a, b = mi()
        a -= 1
        b -= 1
        G[a].add(b)
        G[b].add(a)

    for g in permutations(range(1, N)):
        v = 0
        for nv in g:
            if nv not in G[v]:
                break
            v = nv
        else:
            ans += 1
    print(ans)


def agc024_b():
    N = int(input())
    P = [int(input()) for _ in range(N)]
    Q = {v - 1: i for i, v in enumerate(P)}

    ans_rev = 1
    cur = 1
    prev = Q[0]
    for i in range(1, N):
        if prev < Q[i]:
            cur += 1
        else:
            cur = 1
        prev = Q[i]
        ans_rev = max(ans_rev, cur)
    print(N - ans_rev)


def arc062_b():
    S = input()
    print(len(S) // 2 - S.count("p"))


def diverta2019_2_c():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    res = []
    ma = A[-1]
    mi = A[0]
    for i in range(1, N - 1):
        a = A[i]
        if a < 0:
            res.append((ma, a))
            ma -= a
        else:
            res.append((mi, a))
            mi -= a
    res.append((ma, mi))
    ans = ma - mi
    print(ans)
    for x in res:
        print(*x)


def aising2019_c():
    from itertools import product
    from collections import deque

    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())
    H, W = mi()
    S = [input() for _ in range(H)]
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    uf = UnionFind()
    seen = [[False] * W for _ in range(H)]
    for h, w in product(range(H), range(W)):
        if seen[h][w]:
            continue

        todo = deque([(h, w)])
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 0-indexで考える
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if G[nx][ny] == '#':
                continue
            if seen[nx][ny]:
                continue


if __name__ == '__main__':
    main()
