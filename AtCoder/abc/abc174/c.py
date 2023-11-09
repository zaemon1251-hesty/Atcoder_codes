from math import ceil, log10

K = int(input())
a = 7
ans = 1
if K % 2 == 0:
    print(-1)
    exit()

while a % K != 0 and ans <= 10**7:
    a *= 10
    a += 7
    a %= K
    ans += 1
print(ans if a % K == 0 else -1)
