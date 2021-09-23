def mainc():
    x = list(input())

    r = "A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z ".lower().split()
    x_r = {x[i]: r[i] for i in range(26)}
    r_x = {r[i]: x[i] for i in range(26)}
    N = int(input())
    S = []
    ans = []
    for i in range(N):
        s = list(input())
        encode = ''
        for v in s:
            encode += x_r[v]
        S.append(encode)
    S.sort()
    for p in S:
        decode = ''
        for v in p:
            decode += r_x[v]
        ans.append(decode)
    print(*ans, sep='\n')


def maind():
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


maind()
