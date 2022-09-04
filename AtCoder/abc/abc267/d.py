from math import inf


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [[-inf] * (M + 3) for _ in range(N + 1)]
    dp[0][0] = 0

    for i in range(1, N + 1):
        for j in range(M + 1):
            if (j == 0):
                dp[i][0] = 0
            elif j > i:
                dp[i][j] = -inf
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + j * A[i - 1])
    print(max(dp[i][M] for i in range(M, N + 1)))


if __name__ == '__main__':
    main()
