from functools import reduce
from itertools import accumulate
from math import inf


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


def main():
    N, A, B = map(int, input().split())
    SUM = A + B
    S = input()
    out = []
    for i in range(N):
        if S[i] == "a" and SUM:
            SUM -= 1
            out.append("Yes")
        elif S[i] == "b" and SUM and B:
            SUM -= 1
            B -= 1
            out.append("Yes")
        else:
            out.append("No")
    print(*out, sep="\n")


def sub():
    N = int(input())
    for i in range(N + 1):
        if 108 * i // 100 == N:
            print(i)
            exit()
    print(":(")


def sub2():
    import numpy as np
    N, M, C = map(int, input().split())
    B = list(map(int, input().split())) + [C]
    A = [list(map(int, input().split())) + [1] for _ in range(N)]

    A = np.array(A)
    B = np.array(B)
    C = A.dot(B)

    print(sum(C > 0))


def main2():
    H, W = map(int, input().split())
    if H == 1 or W == 1:
        print(1)
    elif H == 2 or W == 2:
        print(2)
    else:
        print(H // 2 * W + H % 2 * (W + 1) // 2)


def abc065_b():
    N = int(input())
    A = [int(input()) - 1 for _ in range(N)]
    cr = 0
    seen = [True] + [False] * N
    ans = 0

    while cr != 1:
        cr = A[cr]
        if seen[cr]:
            break
        seen[cr] = True
        ans += 1

    if cr == 1:
        print(ans)
    else:
        print(-1)


def agc029_a():
    S = list(input())
    S = list(map(lambda s: 1 if s == "B" else 0, S))

    cnt0 = S.count(0)
    ans = 0
    for s in S:
        if s == 0:
            cnt0 -= 1
        else:
            ans += cnt0
    print(ans)


def agc040_a():
    from itertools import groupby
    from typing import List

    def runLengthEncode(S: str) -> "List[tuple(str, int)]":
        # ランレングス符号化
        grouped = groupby(S)
        res = []
        for k, v in grouped:
            res.append((k, int(len(list(v)))))
        return res

    T = runLengthEncode(input())
    if T[0][0] == ">":
        T = [("<", 0)] + T
    num = len(T)
    ans = 0
    for i in range(num - 1):
        if T[i][0] == "<" and T[i + 1][0] == ">":
            a, b = sorted([T[i][1], T[i + 1][1]])
            ans += a * (a - 1) // 2 + b * (b + 1) // 2
    if T[-1][0] == "<":
        a = T[-1][1]
        ans += a * (a + 1) // 2
    print(ans)


def abc066_b():
    S = input()[:-1]
    N = len(S)
    ans = 0
    for i in range(N - 1):
        for j in range(i + 1, N + 1):
            if (j - i) % 2 == 0:
                k = i + (j - i) // 2
                if S[i:k] == S[k:j]:
                    ans = max(j - i, ans)
    print(ans)


def abc075_b():
    from itertools import product
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    G = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                G[i][j] = "#"
                for x, y in product(range(-1, 2), repeat=2):
                    if x == y == 0:
                        continue
                    nx, ny = i + x, j + y
                    if nx < 0 or nx >= H or ny < 0 or ny >= W:
                        continue
                    if S[nx][ny] == "#":
                        continue
                    G[nx][ny] += 1
    for i in range(H):
        print(*G[i], sep="")


def abc098_b():
    N = int(input())
    S = input()
    ans = 0
    for i in range(N):
        ans = max(len(set(S[:i]) & set(S[i:])), ans)
    print(ans)


def abc064_c():
    from collections import Counter

    N = int(input())
    C = Counter(map(lambda x: int(x) // 400 if (int(x) // 400)
                < 8 else 8, input().split()))
    zero = sum((i not in C) for i in range(8))
    free = C[8]
    fixed = 8 - zero
    if fixed == 0 and free > 1:
        print(1, free)
    else:
        print(fixed, fixed + free)


def abc136_d():
    from itertools import groupby
    from typing import List

    def runLengthEncode(S: str) -> "List[tuple(str, int)]":
        # ランレングス符号化
        grouped = groupby(S)
        res = []
        for k, v in grouped:
            res.append((k, int(len(list(v)))))
        return res

    S = input()
    N = len(S)
    rlgs = runLengthEncode(S)
    num = len(rlgs)
    cr = 0
    ans = [0] * N
    for i in range(0, num, 2):
        r = rlgs[i][1]
        l = rlgs[i + 1][1]
        r_idx = cr + r
        l_idx = r_idx + 1
        ans[r_idx - 1] += r // 2 + r % 2 + l // 2
        ans[l_idx - 1] += r // 2 + l % 2 + l // 2
        cr += r + l
    print(*ans)


def jsc2019_qual_b():
    MOD = 10**9 + 7
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    ans = 0

    for i in range(N - 1):
        for j in range(i + 1, N):
            if A[i] > A[j]:
                ans += K * (K - 1) // 2 + K
            elif A[i] < A[j]:
                ans += K * (K - 1) // 2
            ans %= MOD
    print(ans)


def agc043_a():
    from math import inf

    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    dp = [[inf] * W for _ in range(H)]
    dp[0][0] = int(S[0][0] == "#")
    for x in range(H):
        for y in range(W):
            res = dp[x][y]
            if x > 0:
                f = (S[x - 1][y] == "." and S[x][y] == "#")
                res = min(res, dp[x - 1][y] + f)
            if y > 0:
                f = (S[x][y - 1] == "." and S[x][y] == "#")
                res = min(res, dp[x][y - 1] + f)
            dp[x][y] = res
    print(dp[-1][-1])


def abc086_b():
    a, b = input().split()
    c = int(a + b)
    i = 1
    while i**2 < c:
        i += 1
    if i**2 == c:
        print("Yes")
    else:
        print("No")


def abc074_b():
    N = int(input())
    K = int(input())
    X = list(map(int, input().split()))
    ans = 2 * sum(min(x, K - x) for x in X)
    print(ans)


def abc088_b():
    N = int(input())
    X = sorted(map(int, input().split()), reverse=True)
    s = [0, 0]
    i = 0
    for x in X:
        s[i] += x
        i = 1 - i
    print(s[0] - s[1])


def abc068_b():
    N = int(input())
    i = 1
    while i * 2 <= N:
        i *= 2
    print(i)


def abc139_d():
    N = int(input())
    print((N - 1) * N // 2)


def abc060_b():
    from math import gcd
    A, B, C = map(int, input().split())
    d = gcd(A, B)
    A //= d
    B //= d
    if C % d != 0:
        # A*k + B*l = C となるならば，当然
        # a*k + b*l = c (a = A // GCD(A,B),...) も成り立つはず
        print("NO")
    else:
        C //= d
        if C % B == 0:
            # a * k = c (mod b) において c = 0 ならば，k = 0 となり，
            print("NO")
        else:
            print("YES")


def abc057_b():
    from math import inf
    N, M = map(int, input().split())
    gakusei = [list(map(int, input().split())) for _ in range(N)]
    checkp = [list(map(int, input().split())) for _ in range(M)]
    ans = []
    def diff(x, y): return abs(x[0] - y[0]) + abs(x[1] - y[1])
    for g in gakusei:
        res = inf
        cand = -1
        for i, c in enumerate(checkp):
            d = diff(g, c)
            if d < res:
                cand = i
                res = d
        ans.append(cand + 1)
    print(*ans, sep="\n")


def abc107_b():
    H, W = map(int, input().split())
    A = [list(input()) for _ in range(H)]

    AA = []
    for i in range(H):
        if any(A[i][w] != "." for w in range(W)):
            AA.append(A[i])
    A = AA
    H = len(A)
    AA = []
    for j in range(W):
        if any(A[h][j] != "." for h in range(H)):
            AA.append([A[h][j] for h in range(H)])

    W = len(AA)
    H = len(AA[0])
    ans = [[-1] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            ans[i][j] = AA[j][i]

    for i in range(H):
        print(*ans[i], sep="")


def abc048_b():
    a, b, x = map(int, input().split())
    print(b // x - (a - 1) // x)


def abc076_c():
    failmsg = "UNRESTORABLE"
    S_ = list(input())
    T = list(input())
    S_len = len(S_)
    T_len = len(T)
    if S_len < T_len:
        print(failmsg)
        exit()

    def match(s):
        if len(s) != T_len:
            return False, -1
        q_cnt = 0
        for sw, t in zip(s, T):
            if sw == "?":
                q_cnt += 1
            elif sw != t:
                return False, -1
        return True, q_cnt

    for i in range(S_len - T_len, -1, -1):
        f, q = match(S_[i:i + T_len])
        if f:
            S_[i:i + T_len] = T
            for j in range(S_len):
                if S_[j] == "?":
                    S_[j] = "a"
            print("".join(S_))
            exit()
    print(failmsg)


def arc089_a():
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    S.append([0, 0, 0])
    S.sort(key=lambda x: x[0])

    def diff(x, y): return abs(x[0] - y[0]) + abs(x[1] - y[1])

    for i in range(N):
        dist = diff(S[i][1:], S[i + 1][1:])
        delta = S[i + 1][0] - S[i][0]
        if dist > delta or (dist - delta) % 2 != 0:
            print("No")
            exit()
    print("Yes")


def abc096_c():
    H, W = map(int, input().split())
    A = [list(input()) for _ in range(H)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    for x in range(H):
        for y in range(W):
            if A[x][y] != "#":
                continue
            for di, dj in zip(dx, dy):
                nx, ny = x + di, y + dj
                if nx < 0 or nx >= H or ny < 0 or ny >= W:
                    continue
                if A[nx][ny] == "#":
                    break
            else:
                print("No")
                exit()
    print("Yes")


def keyence2019_b():
    S = input()
    N = len(S)

    for i in range(N - 1):
        for j in range(i, N + 1):
            if S[:i] + S[j:] == "keyence":
                print("YES")
                exit()
    print("NO")


def nikkei2019_2_qual_b():
    from collections import Counter
    MOD = 998244353
    N = int(input())
    D = list(map(int, input().split()))

    g = Counter(D)
    s = max(g.keys())

    if g[0] != 1 or D[0] != 0:
        print(0)
        exit()

    ans = 1
    for i in range(s, 0, -1):
        if (i - 1) not in g:
            print(0)
            exit()
        ans *= pow(g[i - 1], g[i], MOD)
        ans %= MOD
    print(ans)


def abc127_d():
    from collections import defaultdict
    numtable = defaultdict(int)
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for _ in range(M)]

    for a in A:
        numtable[a] += 1
    for b, c in BC:
        numtable[c] += b

    ordered = sorted(
        [(v, t) for v, t in numtable.items()],
        key=lambda x: x[0])

    ans = 0
    cur = 0
    while cur < N:
        v, t = ordered.pop()
        addnum = min(N - cur, t)
        ans += v * addnum
        cur += addnum
    print(ans)


def arc075_a():
    N = int(input())
    S = sorted([int(input()) for _ in range(N)])
    ans = sum(S)
    if ans % 10 == 0:
        for i in range(N):
            if S[i] % 10 != 0:
                print(ans - S[i])
                exit()
        else:
            print(0)
    else:
        print(ans)


def arc073_a():
    N, T = map(int, input().split())
    t = list(map(int, input().split()))
    ans = 0
    for i in range(N - 1):
        ans += min(T, t[i + 1] - t[i])
    ans += T
    print(ans)


def abc088_c():
    C = [list(map(int, input().split())) for _ in range(3)]

    for i in range(2, -1, -1):
        for j in range(3):
            C[i][j] -= C[0][j]
    if all(
        all(C[i][j] == C[i][1] for j in range(3))
        for i in range(3)
    ):
        print("Yes")
    else:
        print("No")


def abc054_b():
    from itertools import product
    N, M = map(int, input().split())
    A = [list(input()) for _ in range(N)]
    B = [list(input()) for _ in range(M)]
    for i, j in product(range(N - M + 1), repeat=2):
        flg = True
        for h, w in product(range(M), repeat=2):
            if A[i + h][j + w] != B[h][w]:
                flg = False
                break
        if flg:
            print("Yes")
            exit()
    print("No")


def abc130_d():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    def interval(A, K):
        # 尺取り法
        # 和がKとなる区間のうち最大の長さを求める
        ans = 0
        _sum = 0
        right = 0
        for left in range(N):
            while right < N and _sum < K:
                _sum += A[right]
                right += 1
            if _sum >= K:
                ans += N - right + 1
            _sum -= A[left]
        return ans
    print(interval(A, K))


def abc057_c():
    N = int(input())
    div = 1
    max_div = 1
    while div * div <= N:
        if N % div == 0:
            max_div = div
        div += 1

    gd1, gd2 = max_div, N // max_div
    cnt = 1
    while gd1 >= 10 or gd2 >= 10:
        gd1 //= 10
        gd2 //= 10
        cnt += 1
    print(cnt)


def diverta2019_b():
    R, G, B, N = map(int, input().split())
    ans = 0
    for r in range(N // R + 1):
        for g in range(N // G + 1):
            b = N - R * r - G * g
            if b >= 0 and b % B == 0:
                ans += 1
    print(ans)


def abc073_c():
    N = int(input())
    A = [input() for _ in range(N)]
    bow = set()
    for w in A:
        if w in bow:
            bow.remove(w)
        else:
            bow.add(w)
    print(len(bow))


def abc126_c():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N + 1):
        if i >= K:
            ans += 1
            continue
        cnt = 0
        while pow(2, cnt) * i < K:
            cnt += 1
        ans += 1 / 2**cnt
    print(ans / N)


def abc125_d():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = sum(a < 0 for a in A)
    A = [abs(a) for a in A]
    if cnt % 2 == 0:
        print(sum(A))
    else:
        print(sum(A) - 2 * min(A))


def diverta2019_c():
    N = int(input())
    S = [input() for _ in range(N)]
    STA_ENB = 0
    EN_A = 0
    ST_B = 0
    ans = 0

    for s in S:
        ans += s.count("AB")
        sb = s[0] == "B"
        sa = s[-1] == "A"
        if sb and sa:
            STA_ENB += 1
        elif sb:
            ST_B += 1
        elif sa:
            EN_A += 1
    ans += max(STA_ENB - 1, 0)
    if STA_ENB > 0 and ST_B > 0:
        ans += 1
        ST_B -= 1
    if STA_ENB > 0 and EN_A > 0:
        ans += 1
        EN_A -= 1
    ans += min(EN_A, ST_B)

    print(ans)


def abc051_c():
    sx, sy, tx, ty = map(int, input().split())
    ans = []

    ans.append("U" * (ty - sy))
    ans.append("R" * (tx - sx))
    ans.append("D" * (ty - sy))
    ans.append("L" * (tx - sx + 1))

    ans.append("U" * (ty - sy + 1))
    ans.append("R" * (tx - sx + 1))
    ans.append("DR")
    ans.append("D" * (ty - sy + 1))
    ans.append("L" * (tx - sx + 1))
    ans.append("U")
    print(*ans, sep="")


def arc080_b():
    H, W = map(int, input().split())
    N = int(input())
    A = list(map(int, input().split()))
    c = [[0] * W for _ in range(H)]

    k = 0
    cnt = 0
    end = H * W - 1 if H % 2 == 1 else (H - 1) * W
    col_i = 0
    op = 1
    while cnt <= H * W - 1:
        cnt += 1
        c[k // W][k % W] = col_i + 1

        A[col_i] -= 1
        if A[col_i] == 0:
            col_i += 1

        if (k % W == 0 and op == -1) or (k % W == W - 1 and op == 1):
            op *= -1
            k += W
        else:
            k = k + op

    for i in range(H):
        print(*c[i], sep=" ")


def abc113_c():
    from heapq import heappop, heappush
    N, M = map(int, input().split())
    pref = [[] for _ in range(N + 1)]
    ans = [-1] * M
    CITY = [list(map(int, input().split())) for _ in range(M)]

    for city_i, (p, y) in enumerate(CITY):
        heappush(pref[p], (y, city_i))

    for pref_i in range(1, N + 1):
        rank = 1
        while pref[pref_i]:
            _, city_i = heappop(pref[pref_i])
            ans[city_i] = "%06d" % pref_i + "%06d" % rank
            rank += 1

    print(*ans, sep="\n")


def arc095_b():
    from bisect import bisect_left
    N = int(input())
    A = sorted(map(int, input().split()))

    idx = bisect_left(A, A[-1] // 2)
    ideal = A[-1] // 2 + 1
    cand = [A[idx], A[min(idx + 1, N - 1)], A[max(0, idx - 1)]]
    cand.sort(key=lambda x: abs(min(x, A[-1] - x) - ideal))
    for cd in cand:
        if cd != A[-1]:
            print(A[-1], cd)
            exit()


def abc110_c():
    from collections import defaultdict
    S, T = input(), input()
    N = len(S)
    base = ord("a")
    swapto = [set() for _ in range(26)]
    swapfrom = [set() for _ in range(26)]

    for i in range(N):
        swapto[ord(T[i]) - base].add(ord(S[i]) - base)
        swapfrom[ord(S[i]) - base].add(ord(T[i]) - base)
    for chi in range(26):
        if len(swapto[chi]) > 1 or len(swapfrom[chi]) > 1:
            print("No")
            exit()
    print("Yes")


def abc110_d():
    from collections import Counter

    def prime_factorize(n):
        a = []
        while n % 2 == 0:
            a.append(2)
            n //= 2
        f = 3
        while f * f <= n:
            if n % f == 0:
                a.append(f)
                n //= f
            else:
                f += 2
        if n != 1:
            a.append(n)
        return a

    class ModCmb:
        """calc combinations on the conditions of a certain mod
        """

        def __init__(self, N, mod=10**9 + 7):
            # 二項係数テーブル
            fact = [1, 1]
            factinv = [1, 1]
            inv = [0, 1]
            for i in range(2, N + 1):
                fact.append((fact[-1] * i) % mod)
                inv.append((mod - inv[mod % i] * (mod // i)) % mod)
                factinv.append((factinv[i - 1] * inv[-1]) % mod)

            # 初期化
            self.MOD = mod
            self.N = N
            self.fact = fact
            self.factinv = factinv
            self.inv = inv

        def cmb(self, n, k):
            if n < k:
                return 0
            if n < 0 or k < 0:
                return 0
            return self.fact[n] * \
                (self.factinv[k] * self.factinv[n - k] % self.MOD) % self.MOD

    N, M = map(int, input().split())
    MOD = 10**9 + 7
    factos = Counter(prime_factorize(M))
    md = ModCmb(2 * 10**5, mod=MOD)
    ans = 0

    ans = 1
    for a in factos.values():
        ans *= md.cmb(N - 1 + a, a)
        ans %= MOD

    print(ans)


def keyence2020_b():
    inf = 1 << 60
    N = int(input())
    robo = []
    for _ in range(N):
        X, L = map(int, input().split())
        robo.append((X - L, X + L))
    robo.sort(key=lambda x: (x[1], x[0]))
    ans = 0
    Redge = -inf
    for l, r in robo:
        if Redge <= l:
            ans += 1
            Redge = r
    print(ans)


def abc084_c():
    def ceil(x, y):
        return (x + y - 1) // y
    N = int(input())
    G = [list(map(int, input().split())) for _ in range(N - 1)]
    ans = [0] * (N)
    for st in range(N - 1):
        # st + 1 駅
        c, s, f = G[st]
        clk = s + c
        curst = st + 1
        while curst < N - 1:
            c, s, f = G[curst]
            if s >= clk:
                clk = s + c
            else:
                clk = s + ceil(clk - s, f) * f + c
            curst += 1
        ans[st] = clk

    print(*ans, sep="\n")


def codefestival_2016_qualC_b():
    K, T = map(int, input().split())
    A = sorted(map(int, input().split()), reverse=True)
    print(max(A[0] - 1 - (K - A[0]), 0))


def agc015_a():
    N, A, B = map(int, input().split())
    print(max(0, (N - 1) * B + A - (N - 1) * A - B + 1))


def arc086_a():
    from collections import Counter
    from heapq import heapify, heappop
    def li(): return list(map(int, input().split()))
    def mi(): return map(int, input().split())
    def ii(): return int(input())

    N, K = mi()
    A = li()
    C = Counter(A)
    cur = len(C.keys())
    ans = 0
    F = map(lambda x: (x[1], x[0]), C.items())
    F = list(F)
    heapify(F)
    while A and cur > K:
        rew, _ = heappop(F)
        cur -= 1
        ans += rew
    print(ans)


def agc013_a():
    def li(): return list(map(int, input().split()))
    def mi(): return map(int, input().split())
    def ii(): return int(input())

    N = ii()
    A = li()
    dA = [A[i + 1] - A[i] for i in range(N - 1)]
    if N <= 2:
        print(1)
        exit()

    ans = 1
    now = 0
    for d in dA:
        if d == 0:
            continue
        elif now < 0 and d > 0:
            ans += 1
            now = 0
        elif now > 0 and d < 0:
            ans += 1
            now = 0
        else:
            now = d
    print(ans)


def agc006_a():
    def li(): return list(map(int, input().split()))
    def mi(): return map(int, input().split())
    def ii(): return int(input())
    N = ii()
    s = input()
    t = input()
    L_t = len(t)
    L_s = len(s)

    for k in range(L_t, -1, -1):
        if k <= L_s and s[-k:] == t[:k]:
            break
    print(L_s + L_t - k)


def arc101_a():
    def li(): return list(map(int, input().split()))
    def mi(): return map(int, input().split())
    def ii(): return int(input())

    N, K = mi()
    X = li()
    pls, mis = [], []
    for x in X:
        if x >= 0:
            pls.append(x)
        else:
            mis.append(-x)

    pls.sort()
    mis.sort()

    Np, Nm = len(pls), len(mis)
    Sp = [0] + pls
    Sm = [0] + mis

    ans = 1 << 60
    for ip in range(min(Np, K) + 1):
        im = K - ip
        if im <= Nm:
            ans = min(ans, 2 * Sm[im] + Sp[ip])

    for im in range(min(Nm, K) + 1):
        ip = K - im
        if ip <= Np:
            ans = min(ans, Sm[im] + 2 * Sp[ip])

    print(ans)


def agc011_b():
    def li(): return list(map(int, input().split()))
    def mi(): return map(int, input().split())
    def ii(): return int(input())

    N = ii()
    A = sorted(li())

    def check(x):
        K = sum(A[:x + 1])
        for enem in range(x + 1, N):
            if A[enem] <= 2 * K:
                K += A[enem]
            else:
                return False
        return True

    ok = N - 1
    ng = -1
    while ok - ng > 1:
        cen = (ok + ng) // 2
        if check(cen):
            ok = cen
        else:
            ng = cen
    print(N - ok)


def agc018_a():
    from math import gcd
    from functools import reduce

    def gcd2(A):
        return reduce(gcd, A)

    def li(): return list(map(int, input().split()))
    def mi(): return map(int, input().split())
    def ii(): return int(input())

    N, K = mi()
    A = li()
    if max(A) < K:
        print("IMPOSSIBLE")
    elif (gcd2(A) == 1) or (K % gcd2(A) == 0):
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")


if __name__ == '__main__':
    agc018_a()
