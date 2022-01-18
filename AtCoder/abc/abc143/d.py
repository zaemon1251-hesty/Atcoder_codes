from bisect import bisect_left, bisect
n = int(input())
d = list(map(int, input().split()))
d.sort()
ans = 0
for i in range(n-1):
    for j in range(i + 1, n):
        w = abs(d[i]-d[j])
        m = d[i] + d[j]
        l = bisect(d[j + 1:], w)
        r = bisect_left(d[j + 1:], m)
        # print(d[i], d[j], d[j + 1:])
        ans += max(0, r - l)
print(ans)
d()
