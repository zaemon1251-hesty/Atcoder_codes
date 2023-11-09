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

    N, S = mi()
    deck = [li() for _ in range(N)]
    dp = [[False] * 20000 for _ in range(N + 1)]
    dp[0][0] = True

    for i in range(N):
        for s in range(S + 1):
            if 0 <= s - deck[i][0]:
                dp[i + 1][s] |= dp[i][s - deck[i][0]]
            if 0 <= s - deck[i][1]:
                dp[i + 1][s] |= dp[i][s - deck[i][1]]

    if dp[N][S]:
        s = S
        ans = []
        for i in range(N, 0, -1):
            if dp[i - 1][s - deck[i - 1][0]]:
                s -= deck[i - 1][0]
                ans.append("H")
            else:
                s -= deck[i - 1][1]
                ans.append("T")
        print("Yes")
        print(*ans[::-1], sep="")
    else:
        print("No")


if __name__ == "__main__":
    main()
