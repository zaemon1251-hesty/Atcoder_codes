from math import inf, sqrt
import math
import sys


def ceil(x, y):
    return (x + y - 1) // y


def floor(x, y):
    return x // y


def input():
    return sys.stdin.readline().rstrip()


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    T = ii()

    for _ in range(T):
        A, B = mi()
        q_set = set()
        q_set.add(0)
        for k in range(1, math.ceil(sqrt(B - 1)) + 1):
            q_set.add(floor((B - 1), k))
            q_set.add(k)

        ans = inf
        for q in q_set:
            k = floor(B - 1, q + 1) + 1
            ans = min((k + 1) * max(0, q + 1 - A) + k * A - B, ans)

        print(ans)


if __name__ == "__main__":
    main()
