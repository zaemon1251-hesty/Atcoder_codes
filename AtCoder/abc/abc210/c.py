from collections import defaultdict
mod = 10**9 + 7
N, K = map(int, input().split())
C = list(map(int, input().split()))
dic = defaultdict(int)
ans = 0
for i in range(K):
    if dic[i] == 0:
        ans += 1
    dic[i] += 1
ma = ans
for i in range(K, N):
    dic[i - K] -= 1
    if dic[i - K] == 0:
        ans -= 1
    if dic[i] == 0:
        ans += 1
    dic[i] += 1
    ma = max(ma, ans)
print(ma)
