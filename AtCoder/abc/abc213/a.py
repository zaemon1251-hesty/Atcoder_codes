n = int(input())
a = list(map(int, input().split()))
b = sorted(a)
for i in range(n):
    if a[i] == b[-2]:
        print(i + 1)
        exit()
