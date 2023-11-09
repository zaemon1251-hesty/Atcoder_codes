import math
from numba import njit

N = int(input())
count = 0


@njit
def a(i):
    j = 1
    while j * j <= i:
        if i % (j * j) == 0:
            p = i // (j * j)
        j += 1
    return p


for i in range(1, N + 1):
    num = a(i)
    j = 1
    b = int(math.sqrt(N // num))
    count += b
print(count)
