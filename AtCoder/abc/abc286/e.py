import sys

inf = 1 << 40


def input():
    return sys.stdin.readline().rstrip()


def main():

    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())
    N = ii()
    A = li()
    S = [input() for _ in range(N)]

    miyage = [[0 for _ in range(N)] for _ in range(N)]
    cost = [[inf for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if S[i][j] == "Y":
                cost[i][j] = 1
                miyage[i][j] = A[i] + A[j]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if cost[i][j] == cost[i][k] + cost[k][j]:
                    minus = A[k] + (A[i] if i == j else 0)
                    if miyage[i][j] < miyage[i][k] + miyage[k][j] - minus:
                        minus = A[k] + (A[i] if i == j else 0)
                        miyage[i][j] = miyage[i][k] + miyage[k][j] - minus

                elif cost[i][j] > cost[i][k] + cost[k][j]:
                    cost[i][j] = cost[i][k] + cost[k][j]
                    minus = A[k] + (A[i] if i == j else 0)
                    miyage[i][j] = miyage[i][k] + miyage[k][j] - minus
    Q = ii()
    que = [li() for _ in range(Q)]
    for u, v in que:
        u -= 1
        v -= 1
        if cost[u][v] < inf:
            print(cost[u][v], miyage[u][v])
        else:
            print("Impossible")


if __name__ == '__main__':
    main()
