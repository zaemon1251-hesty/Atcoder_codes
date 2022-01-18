N = int(input())
A = list(map(int, input().split()))
a = list(enumerate(A))
a.sort(key=lambda x: x[1])
ans = []
for item in a:
    ans.append(item[0] + 1)
print(*ans)
prime_factorize(n):
a = []
while n % 2 == 0:
    a.append(2)
    n //= 2
f = 3
while f * f <= n:
    if n % f == 0:
        a.append(f)
        n //= f
    else:
        f += 2
if n != 1:
    a.append(n)
return a
