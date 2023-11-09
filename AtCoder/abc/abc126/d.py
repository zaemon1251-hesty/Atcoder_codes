import sys

sys.setrecursionlimit(10**6)


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
    G = [[] for _ in range(N)]
    ans = [-1] * N
    for _ in range(N - 1):
        u, v, w = mi()
        u -= 1
        v -= 1
        G[u].append((v, w))
        G[v].append((u, w))

    def dfs(v, f, p):
        ans[v] = f
        for nv, w in G[v]:
            if p == nv:
                continue
            if w % 2 == 0:
                dfs(nv, f, v)
            else:
                dfs(nv, 1 - f, v)

    dfs(0, 0, -1)

    if all(a == 0 for a in ans):
        ans[0] = 1
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
