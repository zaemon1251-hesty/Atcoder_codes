from collections import defaultdict
from itertools import accumulate
import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    if K == 1:
        print(0)
        exit()

    F = [0]
    for i in range(N):
        F.append((F[-1] + A[i]) % K)

    surplus = defaultdict(int)
    ans = 0

    for i in range(N + 1):
        sup = (F[i] - i) % K
        ans += surplus[sup]
        surplus[sup] += 1
        if (0 <= i - K + 1):
            y = (F[i - K + 1] - (i - K + 1)) % K
            surplus[y] -= 1
    print(ans)


if __name__ == '__main__':
    main()
