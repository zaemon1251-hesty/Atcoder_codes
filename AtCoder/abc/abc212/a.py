from bisect import bisect
N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
ans = 10**9
for i in range(N):
    tg = A[i]
    idx = bisect(B, A[i])
    ans = min(ans, abs(tg - B[min(idx, M-1)]),
              abs(tg - B[max(0, idx - 1)]))
print(ans)
