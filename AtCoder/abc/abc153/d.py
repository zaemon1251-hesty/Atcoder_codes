H = int(input())
ans = 1
from math import log2

ans = int(log2(H))
print(pow(2, ans + 1) - 1)
