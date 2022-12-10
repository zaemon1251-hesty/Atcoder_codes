import sys
from math import gcd
from functools import reduce


def custom_gcd(*a):
    return reduce(lambda x, y: gcd(x, y), a)


def input():
    return sys.stdin.readline().rstrip()


def cnt_pow(x, y):
    cnt = 0
    while x % y == 0:
        x //= y
        cnt += 1
    return cnt


def main():
    def li():
        return list(map(int, input().split()))

    def mi():
        return map(int, input().split())

    def ii():
        return int(input())

    N = ii()
    A = li()
    gcd_a = custom_gcd(*A)
    noneed = cnt_pow(gcd_a, 2) + cnt_pow(gcd_a, 3)
    total_cnt = 0
    for i in range(N):
        cnt_2 = cnt_pow(A[i], 2)
        cnt_3 = cnt_pow(A[i], 3)
        total_cnt += cnt_2 + cnt_3
        A[i] //= pow(2, cnt_2) * pow(3, cnt_3)
    if all(a == A[0] for a in A):
        print(total_cnt - noneed * N)
    else:
        print(-1)


if __name__ == '__main__':
    main()
