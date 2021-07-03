def maind():
    N, K = map(int, input().split())
    P = list(map(lambda x:int(x) - 1, input().split()))
    C = list(map(int, input().split()))
    ans = -10**15
    seen = [False]*N
    for i in range(N):
        # if seen[i]:continue
        _max = -10**15
        score = [0]*N
        loop = [0]*N
        town = []
        src = i
        loop[src] = True
        town.append(src)
        cnt = 0

        while True:
            if cnt == K:
                flg = True
                break

            dst = P[src]
            if loop[dst]:
                flg = False
                break

            loop[dst] = True
            score[dst] += score[src] + C[dst]
            _max = max(_max, score[dst])
            cnt += 1
            town.append(dst)
            src = dst
            #seen[dst] = True
        print(f"town: {town}")
        if flg:
            # K回到達
            #print("i:" ,i)
            ans = max(_max, ans)
        else:
            # K回より前にサイクル検出
            new_p = score[town[-1]] + C[dst]
            old_p = score[dst]
            if old_p >= new_p:
                ans = max(_max, ans)
            else:
                idp = town.index(dst)
                chain = len(town[:idp])
                cycle = len(town[idp:])
                p = (new_p - old_p)*((K - chain) // cycle) + sum([score[t] for t in town[:idp + 1]])
                res = (K - chain) % cycle
                cycle_max = new_p - old_p
                for t in town[idp:idp + res + 1]:
                    cycle_max = max(cycle_max, score[t] - old_p)
                ans = max(p + cycle_max, ans, _max)

    print(ans)


def maine():
    R, C, K = map(int, input().split())
    G = [[0]*C for _ in range(R)]
    dp = [[[0]*4 for _ in range(C)]for _ in range(R)]
    for _ in range(K):
        r, c, v = map(int, input().split())
        G[r-1][c-1] = v
        #dp[r-1][c-1][0] = v

    for i in range(R):
        for k in range(3):
            for j in range(C):
                i_prev = max(dp[i-1][j])
                if i==j==0:
                    dp[i][j][k+1] = G[i][j] if k+1 == 1 else 0
                elif i==0:
                    dp[i][j][k+1] = max(dp[i][j][k+1], dp[i][j-1][k+1], dp[i][j-1][k] + G[i][j])
                elif j==0:
                    dp[i][j][k+1] = max(dp[i][j][k+1], i_prev + G[i][j])
                else:
                    dp[i][j][k+1] = max(dp[i][j][k+1], dp[i][j-1][k+1], dp[i][j-1][k] + G[i][j], i_prev + G[i][j])

    print(max(dp[-1][-1]))


if __name__ == "__main__":
    maine()