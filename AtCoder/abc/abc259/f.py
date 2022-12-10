from math import inf
import sys

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    D = list(map(int, input().split()))
    D = [0] + D
    G = [[] for _ in range(N + 1)]
    E = [list(map(int, input().split())) for _ in range(N - 1)]
    for u, v, w in E:
        G[u].append((v, w))
        G[v].append((u, w))
    del E

    dp = [[0, 0] for _ in range(N + 1)]

    def dfs(v, p):
        hq = []
        for nv, w in G[v]:
            if nv == p:
                continue
            dfs(nv, v)
            hq.append(dp[nv][0] + w - dp[nv][1])
            dp[v][0] += dp[nv][1]
            dp[v][1] += dp[nv][1]

        hq.sort(reverse=True)
        for i, diff in enumerate(hq):
            if diff <= 0:
                break
            if i < D[v] - 1:
                dp[v][0] += diff
            if i < D[v]:
                dp[v][1] += diff

        if D[v] == 0:
            dp[v][0] = -inf

    dfs(1, -1)

    print(dp[1][1])


if __name__ == '__main__':
    main()
