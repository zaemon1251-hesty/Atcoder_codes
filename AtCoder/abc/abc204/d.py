from bisect import bisect_left
n = int(input())
t = list(map(int, input().split()))
inf = 10 ** 5
s = sum(t)
s_2 = s / 2
#dp[i][j]: 料理iまでを使ってj分で完成させることができるかどうか
dp = [[False] * (inf+1) for _ in range(n+1)]
dp[0][0] = True
cnd = []
for i in range(1, n+1):
    dish = t[i-1]
    for j in range(inf+1):
        #料理iを選ばない場合
        dp[i][j] = dp[i][j] | dp[i-1][j]
        #料理iを選ぶ場合
        if j-dish >= 0:
            dp[i][j] = dp[i][j] | dp[i-1][j-dish]
        if i == n and dp[i][j]:
            cnd.append(j)
index = bisect_left(cnd, s_2)
cnd1 = max(cnd[index], s-cnd[index])
if index + 1 >= len(cnd):
    print(cnd1)
else:
    cnd2 = max(cnd[index+1], s-cnd[index+1])
    print(min(cnd1, cnd2))
