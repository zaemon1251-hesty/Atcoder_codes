X, Y = map(int, input().split())
from math import ceil
print(max(0, ceil((Y - X) / 10)))
