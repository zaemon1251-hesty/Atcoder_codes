from collections import defaultdict

N, Q = map(int, input().split())
A = list(map(int, input().split()))
dd = defaultdict(list)
ans = []
for i in range(N):
    dd[A[i]].append(i + 1)
for i in range(Q):
    x, k = map(int, input().split())
    if len(dd[x]) < k:
        ans.append(-1)
    else:
        ans.append(dd[x][k - 1])
print(*ans, sep="\n")
