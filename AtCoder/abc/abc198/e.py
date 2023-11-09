import sys

sys.setrecursionlimit(10**6)


def main():
    N = int(input())
    C = list(map(int, input().split()))
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)

    col = {}
    ans = []

    def dfs(x, px):
        if C[x] not in col:
            ans.append(x + 1)

        col[C[x]] = col.get(C[x], 0) + 1
        for nx in G[x]:
            if nx == px:
                continue
            dfs(nx, x)
        col[C[x]] -= 1
        if col[C[x]] == 0:
            col.pop(C[x])

    dfs(0, -1)
    print(*sorted(ans), sep="\n")


if __name__ == "__main__":
    main()
