import sys
from itertools import permutations


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
    for ids in permutations(range(N)):
        T = [S[j] for j in ids]
        flg = True
        for i in range(N - 1):
            if sum(si != ti for si, ti in zip(T[i], T[i + 1])) > 1:
                flg = False
        if flg:
            print("Yes")
            return
    print("No")


if __name__ == "__main__":
    main()
