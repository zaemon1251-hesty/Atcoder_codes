n, k, a = map(int, input().split())
a -= 1
for i in range(k):
    a += 1
    a %= n
if a == 0:
    a = n
print(a)
