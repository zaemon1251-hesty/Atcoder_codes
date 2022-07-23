N, T = map(int, input().split())
P = sorted([tuple(map(int, input().split())) for _ in range(N)])

inf = float("inf")
ans = -inf

dp = [-inf] * (T)
dp[0] = 0
for j in range(N - 1):
    a, b = P[j]

    for k in range(T - 1, a - 1, -1):
        dp[k] = max(dp[k], dp[k - a] + b)

    ans = max(ans, max(dp) + P[j + 1][1])


print(ans)
