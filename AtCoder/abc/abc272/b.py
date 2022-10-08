from itertools import combinations
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
    cnt = [[0] * N for _ in range(N)]
    for _ in range(M):
        k, *X = mi()
        for i, j in combinations(range(k), 2):
            cnt[X[i] - 1][X[j] - 1] += 1

    if all(cnt[i][j] >= 1 for i, j in combinations(range(N), 2)):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
