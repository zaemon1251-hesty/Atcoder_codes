#ABC191-D Circle Lattice Points
import math
F = 10000
def str_process(s):
    if '.' not in s:
        return int(s) * F
    a, b = (s+'0000').split('.')
    return int(a) * F + int(b[:4])


X, Y, R = map(str_process, input().split())
R2 = R*R

def ceil(a, x):
    return ((a + (x-1)) // x) * x

def floor(a, x):
    return (a // x) * x

def sqrt_floor(a):
    ok = 0
    ng = 10 ** 9 + 1
    while ng - ok >= 2:
        mid = ok + (ng - ok) // 2
        if mid ** 2 <= a:
            ok = mid
        else:
            ng = mid
    return ok

ans = 0
for y in range(ceil(Y-R, F), Y+R+1, F):
    T = R2 - (y-Y)**2
    if T < 0: continue
    lower = ceil(X - sqrt_floor(T), F) // F
    upper = floor(X + sqrt_floor(T), F) // F
    ans += max(0, upper - lower + 1)
print(ans)
print(ceil(Y-R,F))
