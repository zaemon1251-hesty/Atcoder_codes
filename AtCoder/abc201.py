#ABC201

def mainD():
    H, W = map(int, input().split())
    G = []
    def fx(x):
        if x=='-':return -1
        else:return 1
    for i in range(H):
        f = list(map(fx, list(input())))
        G.append(f)
    opt = [[0]*(W) for _ in range(H)]

    def operation(i,j):
        if i==H-1 and j==W-1:
            return 0
        elif i == H-1:
            return opt[i][j+1] + G[i][j+1] if (i+j)%2 == 0 else opt[i][j+1] - G[i][j+1]
        elif j == W-1:
            return opt[i+1][j] + G[i+1][j] if (i+j)%2 == 0 else opt[i+1][j] - G[i+1][j]
        else:
            if (i+j)%2==0:
                return max(opt[i][j+1] + G[i][j+1], opt[i+1][j] + G[i+1][j])
            else:
                return min(opt[i][j+1] - G[i][j+1], opt[i+1][j] - G[i+1][j])


    for i in range(H-1, -1, -1):
        for j in range(W-1, -1, -1):
            opt[i][j] = operation(i, j)

    if opt[0][0] > 0:
        print('Takahashi')
    elif opt[0][0] < 0:
        print('Aoki')
    else:
        print('Draw')

def mainE():
    from collections import deque
    N = int(input())
    edge = [[]for i in range(N+1)]
    weight = [[]for i in range(N+1)]
    for i in range(1,N):
        u,v,w = map(int,input().split())
        edge[u].append(v)
        edge[v].append(u)
        weight[u].append(w)
        weight[v].append(w)
    dist = [-1]*(N+1)
    dist[1] = 0
    que = deque([1])
    while que:
        now = que.popleft()
        for i in range(len(edge[now])):
            nex = edge[now][i]
            if dist[nex] == -1:
                dist[nex] = dist[now]^weight[now][i]
                que.append(nex)
    mod = int(1e9+7)
    ans = 0
    for i in range(60):
        cnt = [0]*2
        for j in range(N):
            cnt[dist[j+1]>>i&1] += 1
        ans += (1<<i)*cnt[0]*cnt[1]
        ans %= mod
    print(ans)


if __name__ == "__main__":
    mainE()