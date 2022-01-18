n, k = map(int, input().split())
print(sum(i * 100 * k + k * (k + 1) // 2 for i in range(1, n + 1)))
