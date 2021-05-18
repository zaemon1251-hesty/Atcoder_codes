from bisect import bisect_left, bisect_right
N = int(input())
A = list(map(int, input().split()))
plus = []
minus = []
for i in range(N):
    plus.append(A[i] + i + 1)
    minus.append(A[i] - i - 1)
plus.sort()
minus.sort()
ans = 0
for i in range(N):
    val = -plus[i]
    idx1 = bisect_left(minus, val)
    idx2 = bisect_right(minus, val)
    ans += idx2 - idx1
print(ans)