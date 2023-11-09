# 桁DP
# 大きな数字(10^500000レベル)の加算処理を文字列で行う
X = input()
N = len(X)
dp = list(map(int, list(X)))
for i in range(1, N):
    dp[i] += dp[i - 1]
ans = []
carry = 0
for keta in reversed(dp):
    keta += carry
    carry = keta // 10
    ans.append(keta % 10)
if carry > 0:
    ans.append(carry)
print("".join(map(str, ans[::-1])))
