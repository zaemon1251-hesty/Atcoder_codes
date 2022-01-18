def maind():
    inf = 1 << 60
    N, M = map(int, input().split())
    G = [[inf]*N for _ in range(N)]
    for self in range(N):
        G[self][self] = 0
    for _ in range(M):
        a, b, c = map(int, input().split())
        G[a-1][b-1] = c
    ans = 0
    for k in range(N):
        for i in range(N):
            for j in range(N):
                G[i][j] = min(G[i][k] + G[k][j], G[i][j])
                if G[i][j] < inf:
                    ans += G[i][j]
    print(ans)


maind()
