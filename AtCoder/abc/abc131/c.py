from math import gcd
import sys
def input(): return sys.stdin.readline().rstrip()


def ceil(x, y): return (x + y - 1) // y


def main():
    def li(): return list(map(int, input().split()))
    def mi(): return map(int, input().split())
    def ii(): return int(input())

    A, B, C, D = mi()
    CD = C * D // gcd(C, D)
    TOTAL = B - A + 1
    DIVC = max(B // C - ceil(A, C) + 1, 0)
    DIVD = max(B // D - ceil(A, D) + 1, 0)
    DIVCD = max(B // CD - ceil(A, CD) + 1, 0)

    print(TOTAL - DIVC - DIVD + DIVCD)


if __name__ == '__main__':
    main()
