import sys
from math import gcd


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

    def solve():
        N, D, K = mi()
        n = N // gcd(N, D)
        print((K - 1) // n + ((K - 1) * D) % N)

    for _ in range(T):
        solve()


if __name__ == '__main__':
    main()
