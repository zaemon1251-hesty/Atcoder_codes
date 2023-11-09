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

    N = ii()
    A = li()
    _ = ii()
    B = set(li())
    X = ii()
    dp = [0] * (X + 1)

    dp[0] = 1
    for i in range(X):
        for j in range(N):
            if i in B:
                continue

            if i + A[j] > X:
                continue

            dp[i + A[j]] |= dp[i]

    print("Yes" if dp[X] else "No")


if __name__ == "__main__":
    main()
