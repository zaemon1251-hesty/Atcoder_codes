from math import ceil

t, N = map(int, input().split())
print(N - 1 + ceil(N * 100 / t))
