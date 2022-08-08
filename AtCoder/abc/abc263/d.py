from itertools import accumulate
from math import inf


def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [0, 0, 0]
    for i in range(N):
        dp = [
            dp[0] + L,
            min(dp[0], dp[1]) + A[i],
            min(dp[1], dp[2]) + R
        ]
    print(min(dp))


if __name__ == '__main__':
    main()
