from math import gcd
from functools import reduce
N, M = map(int, input().split())
A = set(map(int, input().split()))
A = list(A)
A = sorted(A)
N = len(A)
r = []
for i in range(N):
    A[i] //= 2
if N==1:
    lcm = A[0]
else:
    lcm = A[0]
    for i in A[1:]:
        lcm = lcm * i // gcd(lcm, i)
if any((lcm//A[i]) % 2 ==0 for i in range(N)):
    print(0)
    exit()
ans = M // lcm // 2
ans += M // lcm % 2
print(ans)
d()