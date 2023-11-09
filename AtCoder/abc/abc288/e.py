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

    n, m = map(int, input().split())

    a = [0] + list(map(int, input().split()))
    c = [0] + list(map(int, input().split()))
    x = set(list(map(int, input().split())))

    INF = 10**18
    dp = [INF] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        new = [INF] * (n + 1)
        ai = a[i]
        mn = float("inf")
        for j in range(i + 1):
            if j == 0:
                if i not in x:
                    new[j] = dp[j]
                continue
            mn = min(mn, c[i - j + 1])
            if i in x:
                new[j] = dp[j - 1] + ai + mn
            else:
                new[j] = min(dp[j], dp[j - 1] + ai + mn)
        dp = new
    print(min(dp))


if __name__ == "__main__":
    main()
