import sys


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
    deg = [0] * N
    for _ in range(M):
        a, _, b, _ = input().split()
        a = int(a) - 1
        b = int(b) - 1
        G[a].append(b)
        G[b].append(a)
        deg[a] += 1
        deg[b] += 1

    seen = [False] * N

    x = y = 0
    for st in range(N):
        if seen[st]:
            continue
        que = [st]
        seen[st] = True
        f = True
        while que:
            v = que.pop()
            if deg[v] != 2:
                f = False
            for u in G[v]:
                if not seen[u]:
                    seen[u] = True
                    que.append(u)
        if f:
            x += 1
        else:
            y += 1

    print(x, y)


if __name__ == "__main__":
    main()
