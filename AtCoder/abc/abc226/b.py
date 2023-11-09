from collections import defaultdict

ans = 0
n = int(input())
A = []
S = defaultdict(set)
for i in range(n):
    A.append(list(map(int, input().split())))
for i in range(n):
    l = A[i][0]
    d = tuple(A[i][1:])
    S[l].add(d)
for k, v in S.items():
    ans += len(v)
print(ans)
