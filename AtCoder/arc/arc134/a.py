n, l, w = map(int, input().split())
a = list(map(int, input().split()))
ans = 0

if a[-1] != l - w:
    a.append(l - w)
    ans += 1
if a[0] != 0:
    a.insert(0, 0)
    ans += 1

for i in range(n - 1 + ans):
    if a[i] + w > a[i + 1]:
        continue
    else:
        d = a[i + 1] - a[i] - w
        ans += (d + w - 1) // w
print(ans)
