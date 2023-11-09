from functools import reduce
from math import gcd


def gcd2(*args):
    return reduce(lambda x, y: gcd(x, y), args)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    mA = min(A)
    B = []
    for a in A:
        if a != mA:
            B.append(a - mA)
    if (B and gcd2(*B) > 1) or all(a % 2 == 0 for a in A) or all(a % 2 == 1 for a in A):
        print(1)
    else:
        print(2)


if __name__ == "__main__":
    main()
