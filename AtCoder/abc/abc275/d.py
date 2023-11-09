from functools import lru_cache
import sys

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline().rstrip()


@lru_cache(None)
def f(x):
    if x == 0:
        return 1
    return f(x // 2) + f(x // 3)


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N = ii()
    print(f(N))


if __name__ == "__main__":
    main()
