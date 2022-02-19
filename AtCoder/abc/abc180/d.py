import sys
from functools import lru_cache
sys.setrecursionlimit(10**6)


def main():
    X, Y, A, B = map(int, input().split())
    ans = 0
    while X * A * (A-1) <= B and X < Y:
        X *= A
        ans += 1
    ans += (Y-X-1) // B
    print(ans)


if __name__ == '__main__':
    main()
