mod = 998244353
N = int(input())
a = list(map(int, input().split()))
dp = [[0] * 10 for _ in range(N)]
dp[0][a[0]] += 1
for i in range(1, N):
    y = a[i]
    for x in range(10):
        dp[i][(x + y) % 10] += dp[i - 1][x]
        dp[i][(x * y) % 10] += dp[i - 1][x]
        dp[i][(x + y) % 10] %= mod
        dp[i][(x * y) % 10] %= mod
for i in range(10):
    dp[-1][i] %= mod
print(*dp[-1], sep="\n")
