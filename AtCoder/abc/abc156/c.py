N = int(input())
X = list(map(int, input().split()))
a = sum(X) // N
b = (sum(X) + N - 1) // N
mina = sum((a - x) ** 2 for x in X)
minb = sum((b - x) ** 2 for x in X)
print(min(mina, minb))
