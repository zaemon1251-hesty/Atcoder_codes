n, k = map(int, input().split())
n %= k
print(min(n, k - n))
