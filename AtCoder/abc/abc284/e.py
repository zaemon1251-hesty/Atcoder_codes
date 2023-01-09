import sys
sys.setrecursionlimit(2 * 10**6)


ans = 0


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

    pths = set()

    def dfs(v):
        global ans
        if ans >= 10**6:
            return
        ans += 1
        pths.add(v)
        for nv in G[v]:
            if nv not in pths:
                dfs(nv)
        pths.remove(v)
    dfs(0)
    print(min(ans, 10**6))


if __name__ == '__main__':
    main()
