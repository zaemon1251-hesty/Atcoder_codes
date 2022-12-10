from collections import deque
from math import inf
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

    N = ii()
    A = li()
    G = [[] for _ in range(2 * N + 2)]
    for i, a in enumerate(A):
        i += 1
        G[a].extend([2 * i, 2 * i + 1])

    ans = [inf] * (2 * N + 2)
    todo = deque([1])
    ans[1] = 0
    while todo:
        v = todo.popleft()
        for nv in G[v]:
            if ans[nv] < inf:
                continue
            ans[nv] = ans[v] + 1
            todo.append(nv)
    print(*ans[1:], sep="\n")


if __name__ == '__main__':
    main()
