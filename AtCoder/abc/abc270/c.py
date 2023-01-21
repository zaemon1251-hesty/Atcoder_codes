import sys


def input():
    return sys.stdin.readline().rstrip()


sys.setrecursionlimit(10**6)

k = []


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())
    N, X, Y = mi()
    E = [li() for _ in range(N - 1)]
    G = [[] for _ in range(N)]
    for u, v in E:
        G[u - 1].append(v - 1)
        G[v - 1].append(u - 1)

    ans = [X - 1]

    def search(v, p):

        if v == Y - 1:
            global k
            k = ans.copy()
            return
        for nv in G[v]:
            if nv == p:
                continue
            ans.append(nv)
            search(nv, v)
            ans.pop()

    search(X - 1, -1)

    for i in range(len(k)):
        k[i] += 1
    print(*k)


if __name__ == '__main__':
    main()
