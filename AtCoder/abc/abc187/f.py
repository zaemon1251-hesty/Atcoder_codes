def main():
    N, M = map(int, input().split())
    G = [0] * N
    for i in range(M):
        A, B = map(int, input().split())
        A -= 1
        B -= 1
        G[A] |= 1 << B
        G[B] |= 1 << A

    dp = [0xff] * (1 << N)
    dp[0] = 1
    for i in range(N):
        for j in range(1 << N):
            if dp[j] == 1 and (G[i] & j) == j:
                dp[j | 1 << i] = 1

    for i in range(1 << N):
        j = i
        while j:
            if dp[i] > dp[j] + dp[i ^ j]:
                dp[i] = dp[j] + dp[i ^ j]
            # 下記の操作で i の部分集合を全探索できる
            j -= 1
            j &= i

    print(dp[-1])


if __name__ == '__main__':
    main()
