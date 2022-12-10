def main():
    MOD = 998244353
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(K)]
    dp = [0]*(N+10)
    sdp = [0]*(N+20)
    dp[0] = 1
    sdp[1] = 1
    for i in range(1, N+1):
        for k in range(K):
            l, r = A[k][0], A[k][1]
            dp[i] += sdp[max(0, i-l+1)] - sdp[max(0, i-r)]
            dp[i] %= MOD
        sdp[i+1] = sdp[i] + dp[i]
        sdp[i+1] %= MOD
    print(dp[N-1] % MOD)


if __name__ == '__main__':
    main()
