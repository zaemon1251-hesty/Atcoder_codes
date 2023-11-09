from collections import defaultdict


def main():
    INF = 1 << 60
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    bonus = defaultdict(int)
    for _ in range(M):
        c, y = map(int, input().split())
        bonus[c] = y

    dp = [[-INF for __ in range(N + 1)] for _ in range(N + 1)]
    dp[0][0] = 0

    for i in range(N):
        dp[i + 1][0] = dp[i][0]
        for cnt in range(1, N + 1):
            dp[i + 1][0] = max(dp[i][cnt], dp[i + 1][0])
            dp[i + 1][cnt] = max(dp[i][cnt - 1] + bonus[cnt] + X[i], dp[i + 1][cnt])
    print(max(dp[N]))


if __name__ == "__main__":
    main()
