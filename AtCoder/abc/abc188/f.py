import sys
from functools import lru_cache

sys.setrecursionlimit(10**6)


def main():
    X, Y = map(int, input().split())

    @lru_cache(None)
    def solve(y):
        if y <= 1:
            return abs(X - y)
        if y % 2 == 0:
            return min(solve(y // 2) + 1, abs(X - y))
        else:
            return min(solve((y + 1) // 2) + 2, solve((y - 1) // 2) + 2, abs(X - y))

    print(solve(Y))


if __name__ == "__main__":
    main()
