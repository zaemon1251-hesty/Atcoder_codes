from copy import deepcopy


def main():
    N, M, K, S, T, X = map(int, input().split())
    S -= 1
    T -= 1
    X -= 1

    MOD = 998244353
    # G = [[]for _ in range(N)]
    E = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]
    E = E + [[v, u] for u, v in E]
    E.sort(key=lambda x: x[0], reverse=True)
    # for u, v in S:
    #     G[u].append(v)
    #     G[v].append(u)
    dp = [[[0] * 2 for _ in range(N)] for _ in range(K + 1)]
    dp[0][S][0] += 1
    for i in range(K):
        for u, v in E:
            if v == X:
                dp[i + 1][v][0] += dp[i][u][1]
                dp[i + 1][v][1] += dp[i][u][0]
            else:
                dp[i + 1][v][0] += dp[i][u][0]
                dp[i + 1][v][1] += dp[i][u][1]
            dp[i + 1][v][0] %= MOD
            dp[i + 1][v][1] %= MOD
    print(dp[K][T][0])


if __name__ == '__main__':
    main()
