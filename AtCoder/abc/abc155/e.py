from math import inf


def main():
    # 桁DP
    S = list(input())[::-1]
    S = list(map(int, S))
    N = len(S)
    dp = [[inf] * 2 for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(N):
        for d in range(2):
            if dp[i][d] != inf:
                c = S[i] + d
                if c != 10:
                    dp[i + 1][0] = min(dp[i + 1][0], dp[i][d] + c)
                dp[i + 1][1] = min(dp[i + 1][1], dp[i][d] + 10 - c)
    print(min(dp[N][1] + 1, dp[N][0]))


if __name__ == '__main__':
    main()
