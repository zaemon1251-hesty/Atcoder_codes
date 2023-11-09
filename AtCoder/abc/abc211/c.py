from collections import defaultdict

mod = 10**9 + 7
S = list(input())
ord = list("chokudai")
dp = [0] * 8
for i in range(len(S)):
    dp[0] += bool(S[i] == ord[0])
    dp[0] %= mod
    for j in range(1, 8):
        if S[i] == ord[j]:
            dp[j] += dp[j - 1]
            dp[j] %= mod
print(dp[-1] % mod)
