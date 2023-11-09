import sys

from itertools import combinations


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
    S = [input() for _ in range(N)]
    cnt = 0
    for i, j in combinations(range(N), 2):
        if all(si == "o" or sj == "o" for si, sj in zip(S[i], S[j])):
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
