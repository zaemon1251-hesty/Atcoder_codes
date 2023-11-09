mod = 998244353
N = int(input())
S = input()
dp = [[0] * 10 for _ in range(1 << 10)]
a = ord("A")
cv = {c: ord(c) - a for c in "ABCDEFGHIJ"}
for c in S:
    x = cv[c]
    # dp=前回の出場|不出場=今回の不出場
    # 今回の出場を加算していく
    # 過去に何らかのコンテストに出場していて
    # 最後にxに出場していたケース
    for bit in range(1 << 10):
        dp[bit][x] += dp[bit][x]
        dp[bit][x] %= mod
    # 過去に何らかのコンテストに出場していて
    # 初めてxに出場するケース
    for bit in range(1 << 10):
        if bit & (1 << x) > 0:
            continue  # xに出場していたら再度出場はできない
        for tail in range(10):
            dp[bit | (1 << x)][x] += dp[bit][tail]
            dp[bit | (1 << x)][x] %= mod
    # 初めて出場するケース
    dp[1 << x][x] += 1
    dp[1 << x][x] %= mod
ans = 0
for bit in range(1 << 10):
    for tail in range(10):
        ans += dp[bit][tail]
        ans %= mod
print(ans)
e()
