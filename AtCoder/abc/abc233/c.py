from itertools import product
from functools import reduce

N, X = map(int, input().split())
La = [list(map(int, input().split())) for _ in range(N)]
L = [i[0] for i in La]
a = [i[1:] for i in La]
ans = 0
for items in product(*a):
    if reduce(lambda x, y: x * y, items) == X:
        ans += 1
print(ans)
