# chs[t] = (delNum, willConn, isConn)
chs = []

# 3 -> ng

# 2 rmv -> ‾
# 上だけを残すので、連結状態であることが前提。遷移後は非連結
chs.append((2, 0, 1))

# 2 rmv -> _
# 同上
chs.append((2, 0, 1))

# 1 rmv -> ‾|
# 上と縦を残す。連結状態であることが前提。遷移後は縦があるので連結になる
chs.append((1, 1, 1))

# 1 rmv -> _|
# 同上
chs.append((1, 1, 1))

# 1 rmv -> ‾_
# 上下を残す。連結かどうかは問わず使えるが、連結状態は継承される
chs.append((1, 1, 1))
chs.append((1, 0, 0))

# 0 rmv -> ‾_|
# 全部残す。連結かどうかは問わずに使うことができ、どんな状態でも連結状態になる
chs.append((0, 1, 0))
chs.append((0, 1, 1))


def main():
    n, p = map(int, input().split())

    # dp[i][j] := i本取り除いた状態で、j=0なら上下が連結、j=1なら非連結
    dp = [[0, 0] for _ in range(n)]
    dp[0][0] = 1
    dp[1][1] = 1
    for _ in range(n - 1):
        dp2 = [[0, 0] for _ in range(n)]
        for i in range(n):
            dp2[i][0] += dp[i][0]
            dp2[i][0] += dp[i][1]
            if i + 1 < n:
                dp2[i + 1][0] += dp[i][0] * 3
                dp2[i + 1][1] += dp[i][1]
            if i + 2 < n:
                dp2[i + 2][1] += dp[i][0] * 2
        for i in range(n):
            dp2[i][0] %= p
            dp2[i][1] %= p
        dp, dp2 = dp2, dp
        # print(dp)

    ans = [x[0] for x in dp]
    print(*ans[1:])


if __name__ == "__main__":
    main()
