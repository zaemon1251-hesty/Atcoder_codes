# 区間スケジューリング問題
from functools import cmp_to_key
inf = 1 << 60
def leftIsBigger(l, r):
    return l[0] * r[1] - r[0] * l[1]
def compare(x, y):
    print(x, y)
    return not leftIsBigger(x[1], y[1])
N = int(input())
S = []
for i in range(N):
    x, y = map(int, input().split())
    A = [(y-1, x), (y, x-1)]
    S.append(A)
S.sort(key=cmp_to_key(compare))
rmax = (0, 1)
ans = 0
for item in S:
    A = item
    if leftIsBigger(A[0], rmax):
        rmax = A[1]
        ans += 1
print(ans)
e()
