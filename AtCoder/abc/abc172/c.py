from bisect import bisect_left
from functools import reduce


N, M, K = map(int, input().split())
*A, = map(int, input().split())
*B, = map(int, input().split())
ans = 0
B = [0] + B
for j in range(M):
    B[j+1] += B[j]

sum_of_A = 0
A = [0] + A
for a in range(N+1):
    sum_of_A += A[a]
    rest = K-sum_of_A
    idxb = bisect_left(B, rest)
    if idxb > M:
        idxb = M
    if B[idxb] > rest:
        idxb -= 1
    if K >= sum_of_A + B[idxb]:
        ans = max(ans, a+idxb)
print(ans)
