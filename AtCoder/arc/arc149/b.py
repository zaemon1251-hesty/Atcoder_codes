from bisect import bisect_left
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
    B = li()

    SORTED_A = sorted(enumerate(A), key=lambda x: (x[1], x[0]))
    iset = [ai[0] for ai in SORTED_A]
    B_ = [B[i] for i in iset]

    INF = 1 << 60
    LIS = [INF] * (N + 1)
    for b in B_:
        i = bisect_left(LIS, b)
        LIS[i] = b

    ANS_B = bisect_left(LIS, INF)
    print(N + ANS_B)


if __name__ == "__main__":
    main()
