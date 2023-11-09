n, x, y = map(int, input().split())

mi = {i: 0 for i in range(1, n)}
for i in range(1, n):
    for j in range(i + 1, n + 1):
        if i <= x and y <= j:
            mi[x - i + 1 + j - y] += 1
        elif x < i and y <= j:
            mi[min(i - x + 1 + j - y, j - i)] += 1
        elif i <= x and j < y:
            mi[min(x - i + 1 + y - j, j - i)] += 1
        elif x < i and j < y:
            mi[min(i - x + 1 + y - j, j - i)] += 1
        else:
            mi[j - i] += 1

for i in range(1, n):
    print(mi[i])
