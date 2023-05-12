import sys
from itertools import product


def input():
    return sys.stdin.readline().rstrip()


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())
    H, W = mi()
    N = min(H, W)
    C = [list(input()) for _ in range(H)]
    dx = [-1, 1, 1, -1]
    dy = [1, -1, -1, 1]

    def direct_cnt(i, j, direct_i):
        assert 0 <= direct_i < 4
        assert C[i][j] == "#"

        direct_0 = 0

        while 0 <= i + dx[direct_i] * direct_0 < H and 0 <= j + dy[direct_i] * direct_0 < W:
            if C[i + dx[direct_i] * direct_0][j + dy[direct_i] * direct_0] == "#":
                direct_0 += 1
            else:
                break

        return direct_0 - 1

    cross = [0] * (N + 1)
    for i, j in product(range(H), range(W)):
        if C[i][j] == "#":
            direct_cnts = [direct_cnt(i, j, direct_i) for direct_i in range(4)]
            if all(c == direct_cnts[0] for c in direct_cnts) and direct_cnts[0] > 0:
                cross[direct_cnts[0]] += 1

    print(*cross[1:])


if __name__ == '__main__':
    main()
