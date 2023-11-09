N = int(input())
A = list(map(int, input().split()))
now = 0
where = [False] * 360

where[now] = True
for i in range(N):
    now += A[i]
    now %= 360
    where[now] = True
t = [i for i in range(360) if where[i]] + [360]
ans = 0
for i in range(len(t) - 1):
    ans = max(t[i + 1] - t[i], ans)
print(ans)
