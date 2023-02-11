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

    N, M = mi()

    G = [[] for _ in range(N)]

    for _ in range(M):
        a, b = mi()
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)

    seen = [False] * N

    def dfs(x, p):
        if len(G[x]) > 2:
            return False
        seen[x] = True
        for nv in G[x]:
            if seen[nv] and nv != p:
                print("No")
                exit(0)
            if seen[nv]:
                continue
            dfs(nv, x)
    dfs(0, -1)

    if all(seen[i] for i in range(N)):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
