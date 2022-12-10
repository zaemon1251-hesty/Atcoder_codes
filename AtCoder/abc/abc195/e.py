N = int(input())
S = list(map(int, input()))
X = input()

dp = [False] * 7
dp[0] = True
for i in range(N - 1, -1, -1):
    if X[i] == "T":
        # 7の倍数にしたい
        newdp = [False] * 7
        for k in range(7):
            newdp[k] = dp[(k * 10) % 7] or dp[(k * 10 + S[i]) % 7]

    else:
        newdp = [True] * 7
        for k in range(7):
            newdp[k] = dp[(k * 10) % 7] and dp[(k * 10 + S[i]) % 7]
    dp, newdp = newdp, dp

print("Takahashi" if dp[0] else "Aoki")
