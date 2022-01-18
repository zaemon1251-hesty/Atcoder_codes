inf = 10**9
N = int(input())
X, Y = map(int, input().split())
dp = [[inf]*(Y+1) for _ in range(X+1)]
S = []
jdx, jdy = 0, 0
for i in range(N):
    tmp = list(map(int, input().split()))
    jdx += tmp[0]
    jdy += tmp[1]
    S.append(tmp)
if jdx < X or jdy < Y:
    print(-1)
    exit()
dp[0][0] = 0
for k in range(N):
    # 大きい順に処理することで更新の重複を防げる
    for i in range(X+1)[::-1]:
        for j in range(Y+1)[::-1]:
            if dp[i][j] == inf:
                continue
            a, b = S[k][0], S[k][1]
            p, q = min(X, i+a), min(Y, j+b)
            dp[p][q] = min(dp[p][q], dp[i][j]+1)
print(dp[-1][-1])
d()
