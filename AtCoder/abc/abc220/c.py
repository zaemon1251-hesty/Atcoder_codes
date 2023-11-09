N = int(input())
a = list(map(int, input().split()))
X = int(input())
s = sum(a)
k = N * (X // s)
r = X % s
i = 0
while r >= 0:
    r -= a[i]
    k += 1
    i += 1
print(min(k, pow(10, 100)))
