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

    N, X = mi()
    S = [li() for _ in range(N)]
    dp = [[False] * (X + 1) for i in range(N + 1)]

    dp[0][0] = True
    for i in range(N):
        A, B = S[i]
        for k in range(X + 1):
            for b in range(B + 1):
                if k + A * b > X:
                    continue
                dp[i + 1][k + A * b] |= dp[i][k]

    print("Yes" if dp[N][X] else "No")


if __name__ == "__main__":
    main()
