# Longest Common Strings ?
def lcs(s, t):
    # 文字列s, t の最長共通部分列の長さ（部分列とは元の文字列から幾つかの要素を、順番を保って取り出して作った文字列）
    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i][j], dp[i - 1][j])
                dp[i][j] = max(dp[i][j], dp[i][j - 1])

    return dp[-1][-1]
