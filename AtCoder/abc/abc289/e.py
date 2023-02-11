import sys
from collections import deque
from itertools import product


def input():
    return sys.stdin.readline().rstrip()


inf = 10**18


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    T = ii()

    def solve():
        N, M = mi()
        C = li()
        G = [[] for _ in range(N)]

        for _ in range(M):
            a, b = mi()
            a -= 1
            b -= 1
            G[a].append(b)
            G[b].append(a)

        short = [[inf] * N for _ in range(N)]
        short[0][N - 1] = 0
        todo = deque([(0, N - 1)])

        # nvij = {}
        # for i, j in combinations(range(N), 2):
        #     if C[i] != C[j]:
        #         nvij[i, j] = product(G[i], G[j])
        #         nvij[j, i] = product(G[j], G[i])

        while todo:
            t, a = todo.popleft()
            for nt, na in product(G[t], G[a]):
                if C[nt] == C[na]:
                    continue
                if short[nt][na] > 1 + short[t][a]:
                    short[nt][na] = 1 + short[t][a]
                    todo.append((nt, na))

        if short[N - 1][0] != inf:
            print(short[N - 1][0])
        else:
            print(-1)

    for _ in range(T):
        solve()


if __name__ == '__main__':
    main()
