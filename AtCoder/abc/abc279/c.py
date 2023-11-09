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

    H, W = mi()
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    SS, TT = [], []
    for y in range(W):
        SS.append("".join([S[i][y] for i in range(H)]))
        TT.append("".join([T[i][y] for i in range(H)]))
    TT.sort()
    SS.sort()

    if all(ss == tt for ss, tt in zip(SS, TT)):
        print("Yes")
        return

    print("No")


if __name__ == "__main__":
    main()
