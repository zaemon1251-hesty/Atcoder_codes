from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))
C = defaultdict(int)
ans = sum(A)
for k in A:
    C[k] += 1

Q = int(input())
for i in range(Q):
    b, c = map(int, input().split())
    ans += C[b] * (c - b)
    C[c] += C[b]
    C[b] = 0
    print(ans)
