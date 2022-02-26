import sys
sys.setrecursionlimit(10**7)


def main():
    A, B, C = map(int, input().split())

    dp = [[[1.0] * (100) for _ in range(100)] for _ in range(100)]

    for i in range(99, -1, -1):
        for j in range(99, -1, -1):
            for k in range(99, -1, -1):
                if i == j == k == 0:
                    continue
                if i > 1:
                    dp[i-1][j][k] += dp[i][j][k] * (i-1)/(i+j+k-1)
                if j > 1:
                    dp[i][j-1][k] += dp[i][j][k] * (j-1)/(i+j+k-1)
                if k > 1:
                    dp[i][j][k-1] += dp[i][j][k] * (k-1)/(i+j+k-1)
    print(dp[A][B][C])


if __name__ == '__main__':
    main()
