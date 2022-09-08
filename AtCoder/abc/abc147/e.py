from math import inf


def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    B = [list(map(int, input().split())) for _ in range(H)]
    diff = [[abs(A[i][j] - B[i][j]) for j in range(W)] for i in range(H)]
    base = 15000
    dp = [[0] * W for _ in range(H)]
    dp[0][0] |= 1 << (base - diff[0][0])
    dp[0][0] |= 1 << (base + diff[0][0])

    for i in range(H):
        for j in range(W):
            if i:
                dp[i][j] |= dp[i - 1][j] >> diff[i][j]
                dp[i][j] |= dp[i - 1][j] << diff[i][j]
            if j:
                dp[i][j] |= dp[i][j - 1] >> diff[i][j]
                dp[i][j] |= dp[i][j - 1] << diff[i][j]

    ans = 10**10

    tmp = dp[-1][-1]
    for i in range(26000):
        if tmp & 1:
            ans = min(ans, abs(i - base))
        tmp >>= 1
    print(ans)


if __name__ == '__main__':
    main()
