from collections import defaultdict
from operator import itemgetter


class Mo:
    def f(self, x: int):
        if x < 0:
            return 0
        return x * (x - 1) * (x - 2) // 6

    def __init__(self, ls):
        from math import sqrt, ceil

        self.ls = ls
        self.n = len(ls)
        self.b = ceil(sqrt(self.n))  # bukectのサイズ及び個数

    def _init_states(self):
        ########################################
        # self.states = None  # その時点における状態(自分で定義しろ) #2つでもいい
        self.result = 0
        self.cnt = defaultdict(lambda: 0)
        ########################################

        # [l,r)の半開区間で考える
        self.l = 0
        self.r = 0

        # queryを格納する用
        self.bucket = [list() for _ in range((self.b + 1))]

    def _add(self, i):
        # i番目の要素を含めて考えるときへstatesを更新
        self.result += self.f(self.cnt[self.ls[i]] + 1) - self.f(self.cnt[self.ls[i]])
        self.cnt[self.ls[i]] += 1

    def _delete(self, i):
        # i番目の要素を削除して考えるときへstatesを更新
        self.result += self.f(self.cnt[self.ls[i]] - 1) - self.f(self.cnt[self.ls[i]])
        self.cnt[self.ls[i]] -= 1

    def _one_process(self, l, r):
        r += 1
        # クエリ[l,r)に対してstatesを更新する
        for i in range(self.r, r):  # rまで伸長
            self._add(i)
        for i in range(self.r - 1, r - 1, -1):  # rまで短縮
            self._delete(i)
        for i in range(self.l, l):  # lまで短縮
            self._delete(i)
        for i in range(self.l - 1, l - 1, -1):  # lまで伸長
            self._add(i)

        self.l = l
        self.r = r

    def process(self, queries):
        self._init_states()

        for i, (l, r) in enumerate(queries):  # queryをbucketに格納
            self.bucket[l // self.b].append((l, r, i))

        for i in range(len(self.bucket)):
            self.bucket[i].sort(key=itemgetter(1))

        ret = [-1] * len(queries)
        for b in self.bucket:
            for l, r, i in b:  # クエリに答えていく
                self._one_process(l, r)
                ########################################
                # クエリに答える作業をここで書く
                ret[i] = self.result
                ########################################
        return ret


def abc293_g():
    def li():
        return list(map(int, input().split()))

    def mi(x=0):
        return map(lambda i: int(i) - x, input().split())

    def ii():
        return int(input())

    N, Q = mi()
    A = li()
    lr = [mi(1) for _ in range(Q)]
    mo = Mo(A)
    print(*mo.process(lr), sep="\n")


def abc073_d():
    from itertools import permutations

    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    inf = 1 << 32

    N, M, R = mi()
    r = li()
    E = [li() for _ in range(M)]

    cost = [[inf] * N for _ in range(N)]

    for a, b, c in E:
        a -= 1
        b -= 1
        cost[a][b] = c
        cost[b][a] = c

    for i in range(N):
        cost[i][i] = 0

    # warshall_floyd
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if cost[i][j] > cost[i][k] + cost[k][j]:
                    cost[i][j] = cost[i][k] + cost[k][j]

    ans = inf
    for p in permutations(r):
        tmp = 0
        for i in range(R - 1):
            x, y = p[i] - 1, p[i + 1] - 1
            tmp += cost[x][y]
        ans = min(ans, tmp)
    print(ans)


def abc099_d():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N, C = mi()
    D = [li() for _ in range(C)]
    c = [li() for _ in range(N)]
    Equivalence_Classes = [[0] * C for _ in range(3)]
    for ci in range(C):
        for i in range(N):
            for j in range(N):
                Equivalence_Classes[(i + j) % 3][ci] += D[c[i][j] - 1][ci]

    ans = 1 << 32
    for ci in range(C):
        for cj in range(C):
            for ck in range(C):
                if ci == cj:
                    continue
                if ci == ck:
                    continue
                if cj == ck:
                    continue
                tmp = 0
                tmp += Equivalence_Classes[0][ci]
                tmp += Equivalence_Classes[1][cj]
                tmp += Equivalence_Classes[2][ck]
                ans = min(ans, tmp)
    print(ans)


def dwacon5th_prelims_c():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N = ii()
    S = list(input())
    Q = ii()
    K = li()

    for k in K:
        dp = [0, 0, 0]  # D, M, (D, M)
        ans = 0
        for i in range(N):
            if S[i] == "D":
                dp[0] += 1
            elif S[i] == "M":
                dp[1] += 1
                dp[2] += dp[0]  # Mが一つ増えたら、Dの数だけ(D, M)の組が増える
            elif S[i] == "C":
                ans += dp[2]
            if i >= k - 1:
                if S[i - k + 1] == "D":
                    dp[2] -= dp[1]  # Dが一つ減ったら、Mの数だけ(D, M)の組が減る
                    dp[0] -= 1

                elif S[i - k + 1] == "M":
                    dp[1] -= 1

        print(ans)


if __name__ == "__main__":
    dwacon5th_prelims_c()
