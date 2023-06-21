import sys
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque
from itertools import accumulate
from heapq import heappop, heappush
from math import inf

sys.setrecursionlimit(10**6)
MOD = 10**9 + 7

stdin = sys.stdin

na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces


# need to pass each other twice, unless both starting on the same position
# simpler question: given their starting positions and initial directions, when will they meet?
# it doesn't matter if one always moves and the other waits, or whether the waiting is split
# 2*l is the minimum
# assumption: always optimal to start on the same position
# meeting point = n-i
# find the closest point to the meeting point
# total = 2*l + 2*(dist of closest point to meeting point)
# 0123456
#   x x
def arc():
    n, l = na()
    A = na()
    ans = inf
    for a in A:
        m = l - a
        i = bisect_right(A, m)
        closest = inf
        if i != len(A):
            closest = abs(m - A[i])
        if i:
            closest = min(closest, abs(m - A[i - 1]))
        # print(A,a,m,i,closest)
        ans = min(ans, 2 * l + 2 * closest)
    print(ans)


def abc051_d():
    # N<100
    # ワーシャルフロイド法でどうだろう
    # ある辺が2つの頂点を直接結ぶが、ワーシャルフロイドでその2点間の距離がより短いとする
    # それならば、その2点を通るあらゆる経路も直接でなく短い方を使うはず

    N, M = map(int, input().split())
    INF = 10**10  # increase upon submission
    distance = [[INF] * N for i in range(N)]

    for i in range(N):
        distance[i][i] = 0

    edge_list = []
    for i in range(M):
        a, b, c = map(int, input().split())
        distance[a - 1][b - 1] = c
        distance[b - 1][a - 1] = c
        edge_list.append((a, b, c))

    for k in range(N):
        for x in range(N):
            for y in range(N):
                distance[x][y] = min(distance[x][y], distance[x][k] + distance[k][y])

    ans = 0
    for a, b, c in edge_list:
        if distance[a - 1][b - 1] < c:
            ans += 1
    print(ans)


def arc079_b():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    K = ii()

    d = K % 50
    n = K // 50
    ans = []
    for _ in range(50 - d):
        ans.append(49 - d)

    for _ in range(d):
        ans.append(50)

    for i in range(50):
        ans[i] = ans[i] + n

    print(len(ans))
    print(*ans)


def arc075_b():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N, A, B = li()
    H = [ii() for _ in range(N)]

    def check(x):
        c = 0
        for i in range(N):
            h = H[i] - B * x
            if h <= 0:
                continue
            c += (h + (A - B) - 1) // (A - B)
        return c <= x

    ng = 0
    ok = 1010101010
    while ok - ng > 1:
        cen = (ok + ng) // 2
        if check(cen):
            ok = cen
        else:
            ng = cen
    print(ok)


if __name__ == "__main__":
    arc075_b()
