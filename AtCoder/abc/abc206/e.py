L, R = map(int, input().split())
A = [0] * (R + 1)
for i in range(2, R + 1)[::-1]:
    if A[i]:continue
    k = R // i - (L - 1) // i
    A[i] = k * (k - 1) // 2
    for p in range(2 * i, R + 1, i):
        A[i] -= A[p]
ans = sum(A)
x = 0
for g in range(max(2, L), R + 1)[::-1]:
    x += max(R // g - 1, 0)
ans -= x
ans *= 2
print(ans)
_name__ =="__main__":
mori = 20
#maina()
#mainb()
#mainc()
#maind()
maine()