N, K = map(int, input().split())
i = 0
while N >= K:
    N //= K
    i += 1
print(i + 1)
