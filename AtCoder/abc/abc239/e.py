import sys
sys.setrecursionlimit(10**6)


def main():
    N, Q = map(int, input().split())
    X = list(map(int, input().split()))
    noods = [[] for i in range(N)]
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)
    Q = [list(map(int, input().split())) for _ in range(Q)]

    def dfs(x, p):
        if x != 0 and len(G[x]) == 1:
            return noods[x]
        for nx in G[x]:
            if nx == p:
                continue
            noods[nx].append(X[nx])
            scores = dfs(nx, x)
            for score in scores:
                noods[x].append(score)
                if len(noods[x]) > 20:
                    noods[x].remove(min(noods[x]))
        return noods[x]

    noods[0].append(X[0])
    dfs(0, -1)
    ans = []

    for v, k in Q:
        v -= 1
        k -= 1
        noods[v].sort(reverse=True)
        ans.append(noods[v][k])

    print(*ans, sep='\n')


if __name__ == '__main__':
    main()
