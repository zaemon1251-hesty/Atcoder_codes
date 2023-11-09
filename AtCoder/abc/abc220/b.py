k = int(input())
a, b = map(str, input().split())
ap = 0
bp = 0
a = a[::-1]
b = b[::-1]
for i in range(len(a)):
    ap += int(a[i]) * pow(k, i)
for i in range(len(b)):
    bp += int(b[i]) * pow(k, i)
print(bp * ap)
