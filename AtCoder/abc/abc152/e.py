import math
N = int(input())
A = list(map(int, input().split()))
mod = 10 ** 9 + 7
lcm = 1
for i in range(N):
    lcm = lcm // math.gcd(lcm, A[i]) * A[i]
lcm %= mod
ans = 0
for i in range(N):
    ie = pow(A[i], mod - 2, mod)
    ans += lcm * ie
    ans %= mod
print(ans)
_name__ == '__main__':
# maina()
# mainb()
# mainc()
# maind()
maine()
