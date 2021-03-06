def maina():
    h, a = map(int, input().split())
    from math import ceil
    print(ceil(h/a))

def mainb():
    h, n = map(int, input().split())
    a = list(map(int, input().split()))
    print("Yes" if h <= sum(a) else "No")

def mainc():
    n, k = map(int, input().split())
    h = sorted(list(map(int, input().split())), reverse = True)
    if k >= n:
        print(0)
    else:
        print(sum(h[k:]))

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
    #mainb()
    mainc()
    #maind()
    #maine()