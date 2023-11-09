import sys

N, K = map(int, input().split())
A = [0] * N
for i in range(K):
    d = int(input())
    p = list(map(int, input().split()))
    for t in p:
        A[t - 1] += 1
ans = []
for i in range(N):
    if A[i] == 0:
        ans.append(i + 1)
print(len(ans))
