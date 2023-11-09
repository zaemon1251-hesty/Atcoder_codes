import sys

sys.setrecursionlimit(10**6)


def main():
    N, X = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    dp = [[False] * (X + 1) for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(1, N + 1):
        for x in range(X + 1):
            if x + A[i - 1][0] <= X:
                dp[i][x + A[i - 1][0]] = dp[i - 1][x] or dp[i][x + A[i - 1][0]]
            if x + A[i - 1][1] <= X:
                dp[i][x + A[i - 1][1]] = dp[i - 1][x] or dp[i][x + A[i - 1][1]]
    print("Yes" if dp[N][X] else "No")


if __name__ == "__main__":
    main()
