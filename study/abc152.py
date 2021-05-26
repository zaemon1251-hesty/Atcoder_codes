def maina():
    n, m = map(int, input().split())
    print("Yes" if n == m else "No")


def mainb():
    a, b = map(int, input().split())
    a, b = str(a) * b, str(b) * a
    print(min(a, b))


def mainc():
    n = int(input())
    p = list(map(int, input().split()))
    min_ = float("inf")
    ans = 0
    for i in range(n):
        if p[i] <= min_:
            ans += 1
            min_ = p[i]
    print(ans)


def maind():
    H = int(input())
    ans = 1
    from math import log2
    ans = int(log2(H))
    print(pow(2, ans + 1) - 1)

def maine():
    from math import ceil
    h, n = map(int, input().split())
    A, B = [], []
    for i in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)


    dp = [[float("inf")] * (h + 1) for _ in range(n)]

    dp[0][0] = 0
    for j in range(1, h + 1):
        dp[0][j] = ceil(j / A[0]) * B[0]

    for i in range(1, n):
        dp[i][0] = 0
        for j in range(1, h + 1):
            dp[i][j] = min(dp[i][j], dp[i - 1][j], ceil(j / A[i]) * B[i], dp[i][max(0, j - A[i])] + B[i]) #min(dp[i - 1][:max(0, j - A[i]) + 1])

    print(dp[-1][-1])

if __name__ == '__main__':
    #maina()
    mainb()
    #mainc()
    #maind()
    #maine()