def gcd(m, n):
    r = m % n
    return gcd(n, r) if r else n


n = int(input())
s = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            s += gcd(gcd(i, j), k)
print(s)
