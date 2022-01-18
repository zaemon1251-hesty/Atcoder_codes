n, k = map(int, input().split())
a=[]
for i in range(n):
    n1, k1 = map(int, input().split())
    a.append((n1,k1))
a = sorted(a, key = lambda x:x[0])
for i in range(n):
    path = a[i][0] - a[i - 1][0] if i >= 1 else a[i][0]
    if k >= path:
        k -= path
        k += a[i][1]
    else:
        print(a[i - 1][0] + k if i >= 1 else k)
        exit()
else:
    print(min(a[i][0] + k, 10**100))
