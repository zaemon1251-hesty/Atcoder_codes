from copy import copy
import sys

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline().rstrip()


seen = set()


def main():
    def li():
        return tuple(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N = ii()
    A = set([li() for _ in range(N)])

    dxy = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1)]

    def dfs(x, y):
        global seen
        if (x, y) in seen:
            return
        seen.add((x, y))
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in seen and (nx, ny) in A:
                dfs(nx, ny)

    ans = 0
    for x, y in A:
        if (x, y) not in seen:
            ans += 1
        dfs(x, y)
    print(ans)


if __name__ == "__main__":
    main()
