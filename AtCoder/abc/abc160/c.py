k, n = map(int, input().split())
a = list(map(int, input().split()))
max_ = 0
for i in range(n):
    max_ = max(max_, (a[i] - a[i - 1] + k) % k)
print(k - max_)
