from math import gcd
n = int(input())
a = []
ans = set()
for _ in range(n):
    a.append(list(map(int, input().split())))
for i in range(n-1):
    for j in range(i + 1, n):
        x, y = a[i][0] - a[j][0], a[i][1] - a[j][1]
        x, y = x//gcd(x, y), y//gcd(x, y)
        ans.add((x, y))
        ans.add((-x, -y))
print(len(ans))
