from itertools import permutations
N = int(input())
cnt = [[0]*10 for _ in range(10)]
for b in range(1, N + 1):
    x, y = get_nums(b)
    cnt[x][y] += 1
ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        ans += cnt[i][j]*cnt[j][i]
print(ans)
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
