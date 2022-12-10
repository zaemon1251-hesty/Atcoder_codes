from math import inf
import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N, M = mi()
    A = li()
    # __getitem__ を一度に3回呼ぶ羽目になることを防ぐ
    dp0 = [[inf for _ in range(M + 1)] for _ in range(N + 1)]
    dp1 = [[inf for _ in range(M + 1)] for _ in range(N + 1)]
    dp1[0][0] = 0
    for i in range(N):
        for j in range(M + 1):
            nxj = j + A[i]
            dp0[i + 1][j] = min(
                dp0[i + 1][j], dp0[i][j], dp1[i][j] + 1)
            if nxj <= M:
                dp1[i + 1][nxj] = min(
                    dp1[i + 1][nxj], dp0[i][j], dp1[i][j])

    for x in range(1, M + 1):
        print(min(dp0[N][x], dp1[N][x]) if min(
            dp0[N][x], dp1[N][x]) < inf else -1)


if __name__ == '__main__':
    main()
