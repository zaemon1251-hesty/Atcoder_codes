import math
import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = [set() for _ in range(M)]

    for i in range(1, N + 1):
        ai = A[i - 1]
        s = (2 * (10**5) - ai) // i
        ss = math.ceil(-ai / i)
        for k in range(max(1, ss), min(s, M) + 1):
            if 0 <= ai + k * i <= 2 * (10**5):
                ans[k - 1].add(ai + k * i)

    for i in range(M):
        for j in range(2 * (10**5) + 1):
            if j not in ans[i]:
                print(j)
                break


if __name__ == "__main__":
    main()
