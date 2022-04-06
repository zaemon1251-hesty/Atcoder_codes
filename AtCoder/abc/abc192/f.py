def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))

    ans = X - max(A)
    for i in range(2, N + 1):
        # dp[j][r] = 魔法力の合計をiで割ったあまりがrになる、j個の魔法力の合計の最大値
        dp = [[-1] * i for _ in range(i + 1)]
        # 魔法力の合計をiで割ったあまりが0になる、0個の魔法力の合計の最大値は0である。(初期値)
        dp[0][0] = 0
        for a in A:
            for j in range(i - 1, -1, -1):
                for k in range(i):
                    if dp[j][k] != -1:
                        dp[j + 1][(k + a) % i] = \
                            max(dp[j + 1][(k + a) % i], dp[j][k] + a)
        need = X % i
        #print(i, dp[i][need])
        if dp[i][need] != -1:
            ans = min(ans, (X - dp[i][need]) // i)
    print(ans)


if __name__ == '__main__':
    main()
