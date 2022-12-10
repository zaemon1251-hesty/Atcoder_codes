n, m = map(int, input().split())
a = list(map(int, input().split()))
print(-1 if n - sum(a) < 0 else n - sum(a))
