from heapq import heappop, heappush
from itertools import product
from math import inf
import sys


def input():
    return sys.stdin.readline().rstrip()


def get_sqrt(x):
    ok = 0
    ng = 10**9 + 1

    while ng - ok > 1:
        cen = (ok + ng) // 2
        if cen**2 <= x:
            ok = cen
        else:
            ng = cen

    return ok


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N, M = mi()

    actions = set()

    for x, y in product(range(get_sqrt(M) + 1), repeat=2):
        if x**2 + y**2 == M:
            for fx, fy in product([-1, 1], repeat=2):
                actions.add((fx * x, fy * y))

    ans = [[inf] * N for _ in range(N)]

    todo = [(0, (0, 0))]
    ans[0][0] = 0
    while todo:
        cnt, (x, y) = heappop(todo)

        if cnt > ans[x][y]:
            continue

        for dx, dy in actions:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            newcnt = cnt + 1
            if newcnt < ans[nx][ny]:
                ans[nx][ny] = newcnt
                heappush(todo, (newcnt, (nx, ny)))

    for i in range(N):
        ans[i] = map(lambda x: x if x < inf else -1, ans[i])
        ans[i] = list(ans[i])
        print(*ans[i])


if __name__ == "__main__":
    main()
