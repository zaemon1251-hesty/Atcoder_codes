from math import ceil
h, n = map(int, input().split())
A, B = [], []
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
dp = [[float("inf")] * (h + 1) for _ in range(n)]
dp[0][0] = 0
for j in range(1, h + 1):
    dp[0][j] = ceil(j / A[0]) * B[0]
for i in range(1, n):
    dp[i][0] = 0
    for j in range(1, h + 1):
        dp[i][j] = min(dp[i][j], dp[i - 1][j], ceil(j / A[i]) * B[i], dp[i]
                       [max(0, j - A[i])] + B[i])  # min(dp[i - 1][:max(0, j - A[i]) + 1])
print(dp[-1][-1])
= 1 << 60
