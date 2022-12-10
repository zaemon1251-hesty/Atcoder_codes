from functools import lru_cache
import sys
sys.setrecursionlimit(10**6)


def main():
    N, X, Y = map(int, input().split())

    @lru_cache(None)
    def r(n):
        if n == 1:
            return 0
        return r(n - 1) + b(n) * X

    @lru_cache(None)
    def b(n):
        if n == 1:
            return 1
        return r(n - 1) + b(n - 1) * Y

    print(r(N))


if __name__ == '__main__':
    main()
