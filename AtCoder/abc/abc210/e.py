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
<<<<<<< HEAD
=======
_name__ == "__main__":
mori = 20
# maina()
# mainb()
# mainc()
maind()
# maine()
>>>>>>> f9ad35ec977c779c25cb6b4ce6092c52d1b94ee0
