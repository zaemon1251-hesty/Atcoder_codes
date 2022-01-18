MOD = 998244353
H, W, K = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
dp = [0]*4  # (x2,y2),(x2,any),(any,y2),(any,any)
if x1 == x2 and y1 == y2:
    dp[0] = 1
elif x1 == x2:
    dp[1] = 1
elif y1 == y2:
    dp[2] = 1
else:
    dp[3] = 1
for _ in range(K):
    nexts = [
        (dp[1]+dp[2]) % MOD,
        (dp[0]*(W-1) % MOD+dp[1]*(W-2) % MOD+dp[3]) % MOD,
        (dp[0]*(H-1) % MOD+dp[2]*(H-2) % MOD+dp[3]) % MOD,
        (dp[1]*(H-1)+dp[2]*(W-1)+dp[3]*(H+W-4)) % MOD
    ]
    dp = nexts
print(dp[0])
e()
