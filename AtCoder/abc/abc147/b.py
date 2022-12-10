mod = 10**9+7
n = int(input())
a = list(map(int, input().split()))
d = [0]*60
ans = 0
for j in range(60):
    pr = 0
    ng = 0
    for i in range(n):
        if (a[i] >> j) & 1:
            pr += 1
        else:
            ng += 1
    ans += pr*ng*pow(2, j)
    ans %= mod
print(ans % mod)
_name__ == "__main__":
# mainc()
maind()
