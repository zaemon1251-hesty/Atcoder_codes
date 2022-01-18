from math import ceil
a, b, c, d = map(int, input().split())
if d * c <= b:
    print(-1)
else:
    print(ceil(a / (d * c - b)))
