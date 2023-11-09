from collections import defaultdict, Counter
from itertools import accumulate

N, K = map(int, input().split())
A = list(map(int, input().split()))
acc = list(accumulate(A))
acc.insert(0, 0)
C = Counter(acc)
ans = 0
if K != 0:
    for i in range(N + 1):
        ans += C[acc[i] + K]
        C[acc[i]] -= 1
else:
    for key, value in C.items():
        ans += (value * (value - 1)) // 2
print(ans)
d()
