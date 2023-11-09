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

    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for i in range(N):
        B[i + 1] = B[i] + A[i // 2]
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(i):
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j])
            dp[i + 1][0] = max(dp[i + 1][0], dp[i][j] + B[j])
    ans = 0
    for i in range(N):
        ans = max(ans, dp[N][i] + B[i])
    print(ans)


if __name__ == "__main__":
    main()
