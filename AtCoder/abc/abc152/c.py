n = int(input())
p = list(map(int, input().split()))
min_ = float("inf")
ans = 0
for i in range(n):
    if p[i] <= min_:
        ans += 1
        min_ = p[i]
print(ans)
