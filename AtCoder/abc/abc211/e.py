from math import gcd
N, M = map(int, input().split())
D = []
for i in range(M):
    a, c = map(int, input().split())
    D.append((a, c))
D.sort(key=lambda x: x[1])
ans = 0
X = N
#sdgs = N
for i in range(M):
    a, c = D[i][0], D[i][1]
    tmp = gcd(X, a)
    ans += c * (X - tmp)
    X = tmp
print(ans if X == 1 else -1)
_name__ == "__main__":
mori = 20
# maina()
# mainb()
# mainc()
maind()
# maine()
