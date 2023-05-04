<<<<<<< HEAD
n = int(input())
if n < 40:
    print(40 - n)
elif n < 70:
    print(70 - n)
elif n < 90:
    print(90 - n)
else:
    print("expert")
=======
x = list(input())
r = "A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z ".lower().split()
x_r = {x[i]: r[i] for i in range(26)}
r_x = {r[i]: x[i] for i in range(26)}
N = int(input())
S = []
ans = []
for i in range(N):
    s = list(input())
    encode = ''
    for v in s:
        encode += x_r[v]
    S.append(encode)
S.sort()
for p in S:
    decode = ''
    for v in p:
        decode += r_x[v]
    ans.append(decode)
print(*ans, sep='\n')
>>>>>>> f9ad35ec977c779c25cb6b4ce6092c52d1b94ee0
