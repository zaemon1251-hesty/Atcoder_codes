inf = 1 << 60


def main():
    N, M, L = map(int, input().split())
    E = [list(map(int, input().split())) for _ in range(M)]
    Q = int(input())
    sten = [list(map(int, input().split())) for _ in range(Q)]
    dist = [[inf] * N for i in range(N)]

    for i in range(N):
        dist[i][i] = 0
    for a, b, c in E:
        dist[a - 1][b - 1] = dist[b - 1][a - 1] = c

    # ワ―シャルフロイド
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])

    for i in range(N):
        for j in range(N):
            if i != j:
                if dist[i][j] <= L:
                    # 補給なしで到達可能
                    dist[i][j] = 1
                else:
                    # 補給なしでは到達不可能
                    dist[i][j] = inf
            else:
                dist[i][j] = 0

    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])

    for s, g in sten:
        s -= 1
        g -= 1
        print(dist[s][g] - 1 if dist[s][g] < inf else -1)


if __name__ == "__main__":
    main()
