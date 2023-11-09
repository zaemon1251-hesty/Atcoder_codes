from math import sqrt, floor

N = int(input())
if N == 1:
    print(1)
    exit()
ans = 0
for a in range(1, floor(sqrt(N))):
    z = N / a
    # print(a, z)
    for b in range(a, floor(sqrt(z)) + 1):
        ans += floor(z / b) - b + 1
print(ans)
