import sys

from math import sqrt, ceil, floor


def input():
    return sys.stdin.readline().rstrip()


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    A, B = mi()

    def f(t):
        return B * t + A / sqrt(t + 1)

    t = (A / 2 / B)**(2 / 3) - 1
    print(min(f(max(floor(t), 0)), f(ceil(t))))


if __name__ == '__main__':
    main()
