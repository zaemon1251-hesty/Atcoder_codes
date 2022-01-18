n, k, m = map(int, input().split())
A = list(map(int, input().split()))
print(max(0, m * n - sum(A)) if m * n - sum(A) <= k else -1)
