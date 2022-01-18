n = int(input())
from collections import Counter
from bisect import bisect_left, bisect_right
A = sorted(list(map(int, input().split())))
B = list(map(int, input().split()))
C = Counter(list(map(lambda x:int(x) - 1, input().split())))
ans = 0
for k,v in C.items():
    val = B[k]
    ans += v * (bisect_right(A, val) - bisect_left(A, val))
print(ans)
