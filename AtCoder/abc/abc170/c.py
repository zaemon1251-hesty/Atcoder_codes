X, N = map(int, input().split())
P = list(map(int, input().split()))
A = [False] * 101
for i in P:
    A[i] = True
ans = 0
for i in range(101):
    if not A[i] and abs(ans - X) > abs(i - X):
        ans = i
print(ans)
