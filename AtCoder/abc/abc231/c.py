from bisect import bisect_left
N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
ans = []
for i in range(Q):
    x = int(input())
    idx = bisect_left(A, x)
    ans.append(N - idx)
print(*ans, sep="\n")
