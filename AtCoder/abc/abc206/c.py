from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
d = defaultdict(int)
for i in range(N):
    d[A[i]] += 1
ans = 0
for k, v in d.items():
    ans += v * (v - 1) // 2
print(ans)
