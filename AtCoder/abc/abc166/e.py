from collections import Counter

N = int(input())
A = list(map(int, input().split()))

P = [-A[i] - i for i in range(N)]
P = Counter(P)
Q = [A[i] - i for i in range(N)]
Q = Counter(Q)

ans = 0
for k, v in P.items():
    if k in Q:
        ans += v * Q[k]
print(ans)
