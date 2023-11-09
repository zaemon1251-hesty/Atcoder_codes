from collections import Counter


N = int(input())
P = list(map(int, input().split()))
k = 10**6 + 10
A = [False] * (k)
F = [False] * (k)
ans = 0
P.sort()
for t in range(N):
    i = P[t]

    if A[i] > 0:
        continue
    for j in range(i * 2, k, i):
        A[j] = True

    if F[i]:
        A[i] = True
    F[i] = True

for t in range(N):
    if not A[P[t]]:
        ans += 1
print(ans)
