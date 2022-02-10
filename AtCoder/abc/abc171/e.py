from functools import reduce


N = int(input())
A = list(map(int, input().split()))
t = reduce(lambda x, y: x ^ y, A)
A = map(lambda x: x ^ t, A)
print(*A)
