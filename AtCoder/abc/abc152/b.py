a, b = map(int, input().split())
a, b = str(a) * b, str(b) * a
print(min(a, b))
