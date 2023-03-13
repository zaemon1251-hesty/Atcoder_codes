import sys
from collections import deque


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
    E = [list(map(lambda x:x - 1, li())) for _ in range(M)]
    G = [[] for _ in range(N)]

    for u, v in E:
        G[u].append(v)

    ans = 0
    for i in range(N):
        f = [False] * N
        f[i] = True
        todo = deque([i])
        while todo:
            v = todo.popleft()
            for nv in G[v]:
                if f[nv]:
                    continue
                f[nv] = True
                ans += 1
                todo.append(nv)

    ans -= M
    print(ans)


if __name__ == '__main__':
    main()
