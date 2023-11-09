from collections import deque

inf = 1 << 60


def e_takahashi_and_animals(INF=float("inf")):
    N = int(input())
    A = [0] + [int(_) for _ in input().split()]

    ans = INF
    dp = [[0] * 2 for _ in range(N + 1)]
    for t in range(2):
        dp[1][t] = A[1] * t
        dp[1][1 - t] = INF

        for i in range(2, N + 1):
            dp[i][0] = dp[i - 1][1]
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][1]) + A[i]

        if t == 0:
            ans = min(ans, dp[N][1])

        if t == 1:
            ans = min(ans, min(dp[N][0], dp[N][1]))
    return ans


def main():
    print(e_takahashi_and_animals())


if __name__ == "__main__":
    main()
