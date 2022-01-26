from collections import deque


n, k, c = map(int, input().split())
s = list(input())
inf = 1 << 60
dp = [-inf] * (n + 1)
pre = [[] for _ in range(n + 1)]
dpt = [[] for _ in range(k + 1)]
seen = [False] * (n + 1)
que = deque([])
ans = []

dp[0] = 0
for i in range(n):
    # i 日目働かないオプション
    if dp[i + 1] < dp[i]:
        dp[i + 1] = dp[i]
        pre[i + 1].clear()
    if dp[i + 1] == dp[i]:
        pre[i + 1].append(i)
    # i 日目働くオプション
    if s[i] == "o":
        to = min(n, i + 1 + c)
        if dp[to] < dp[i] + 1:
            dp[to] = dp[i] + 1
            pre[to].clear()
        if dp[to] == dp[i] + 1:
            pre[to].append(i)
if k < dp[n]:
    print()
    exit()

seen[n] = True
que.append(n)

while que:
    cu = que.popleft()
    for v in pre[cu]:
        if not seen[v]:
            seen[v] = True
            que.append(v)
        # v 日目働くとき、v日目までの最大勤務日数が dp[v] になる
        if dp[v] + 1 == dp[cu]:
            dpt[dp[v]].append(v + 1)

for i in range(k):
    if len(dpt[i]) == 1:
        ans.append(dpt[i][0])

print(*sorted(ans), sep="\n")
