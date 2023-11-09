import math
from itertools import combinations, product
from functools import reduce, lru_cache
from collections import defaultdict
from operator import itemgetter


class UnionFind:
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
        return "\n".join("{}: {}".format(r, self.members(r)) for r in self.roots())


def arc107_c():
    MOD = 998244353

    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N, K = mi()

    @lru_cache(None)
    def exlp(n):
        if n == 0:
            return 1

        return (n * exlp(n - 1)) % MOD

    A = [li() for _ in range(N)]

    uf1 = UnionFind(N)
    uf2 = UnionFind(N)

    for i, j in combinations(range(N), 2):
        if all(A[i][x] + A[j][x] <= K for x in range(N)):
            uf1.union(i, j)
        if all(A[x][i] + A[x][j] <= K for x in range(N)):
            uf2.union(i, j)

    ans = 1

    rows = [-uf1.parents[i] for i in range(N) if uf1.parents[i] < 0]
    cols = [-uf2.parents[i] for i in range(N) if uf2.parents[i] < 0]

    for y in rows:
        ans *= exlp(y)
        ans %= MOD
    for y in cols:
        ans *= exlp(y)
        ans %= MOD

    print(ans)


def agc048_a():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    INF = 10**18

    T = ii()

    def solve():
        S = input()
        ans = INF
        if all(s == "a" for s in S):
            print(-1)
            return
        if S > "atcoder":
            print(0)
            return

        for i, s in enumerate(S):
            if s == "a":
                continue
            if s > "t":
                ans = min(ans, i - 1)
            else:
                ans = min(ans, i)

        print(ans if ans < INF else -1)

    for _ in range(T):
        solve()


def abc100_d():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N, M = mi()
    S = [li() for _ in range(N)]

    def solve(f):
        S.sort(key=lambda x: sum(fi * i for i, fi in zip(x, f)), reverse=True)

        X, Y, Z = 0, 0, 0
        for x, y, z in S[:M]:
            X += x
            Y += y
            Z += z
        return abs(X) + abs(Y) + abs(Z)

    print(max(solve(f) for f in product([-1, 1], repeat=3)))


def sumitb2019_e():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    _ = ii()
    A = li()
    MOD = 1000000007

    nums = defaultdict(lambda: 0)
    nums[0] += 3

    ans = 1
    for a in A:
        ans *= nums[a]
        ans %= MOD
        nums[a] -= 1
        nums[a + 1] += 1
    print(ans)


def arc058_a():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N, K = mi()
    D = set(li())

    while N < 10**7:
        for i in str(N):
            if int(i) in D:
                break
        else:
            break
        N += 1

    print(N)


def arc096_b():
    ans = 0
    n, c = map(int, input().split())
    XV = [tuple(map(int, input().split())) for _ in range(n)]
    R = [
        0,
    ]
    RR = [
        0,
    ]
    tmp = 0
    pre = 0

    for x, v in XV:
        tmp += v - (x - pre)
        R.append(max(R[-1], tmp))
        RR.append(max(RR[-1], tmp - x))
        ans = max(ans, tmp)
        pre = x

    tmp = 0
    pre = c

    for i, (x, v) in enumerate(XV[::-1], 2):
        tmp += v - (pre - x)
        ans = max([ans, tmp, R[-i] + tmp - (c - x), RR[-i] + tmp])
        pre = x

    print(ans)


def arc159_a():
    from math import inf

    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N, K = mi()
    A = [li() for _ in range(N)]
    cost = [[inf] * N for _ in range(N)]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if cost[i][j] == inf and A[i][j] == 1:
                    cost[i][j] = 1
                else:
                    if cost[i][j] > cost[i][k] + cost[k][j]:
                        cost[i][j] = cost[i][k] + cost[k][j]

    Q = ii()
    for i in range(Q):
        s, t = mi()
        s -= 1
        t -= 1
        if cost[s % N][t % N] < inf:
            print(cost[s % N][t % N])
        else:
            print(-1)


def prime(n):
    prime_list = []
    # 素数で割り切れるかの判定
    for p in range(2, int(n**0.5) + 1):
        if n % p == 0:
            prime_list.append(p)
            while n % p == 0:
                n //= p
    # n が1より大きい数字として残っていれば、素数
    if n != 1:
        prime_list.append(n)
    return prime_list


def arc159_b():
    A, B = map(int, input().split())
    if A < B:
        A, B = B, A
    if A == B:
        print(1)
        return
    ans = 0
    while A > 0 and B > 0:
        if A - B == 1:
            ans += min(A, B)
            break
        else:
            g = math.gcd(A, B)
            A = A // g
            B = B // g
            if A - B == 1:
                ans += min(A, B)
                break
            prime_list = prime(A - B)
            t = float("inf")
            for p in prime_list:
                t = min(t, B % p)
            A -= t
            B -= t
            ans += t
    print(ans)


if __name__ == "__main__":
    arc159_b()
