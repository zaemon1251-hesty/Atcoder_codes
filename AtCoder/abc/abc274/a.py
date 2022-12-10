# from decimal import Decimal
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
    A, B = mi()
    if A == B:
        print("1.000")
    else:
        print("0." + "%03d" % (round(B * 1000 / A)))


if __name__ == '__main__':
    main()
