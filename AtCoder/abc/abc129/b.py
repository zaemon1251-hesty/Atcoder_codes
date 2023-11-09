from itertools import accumulate
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

    _ = ii()
    W = li()
    S = list(accumulate(W))
    total = S[-1]
    ans = inf
    for s in S:
        ans = min(abs(total - 2 * s), ans)
    print(ans)


if __name__ == "__main__":
    main()
