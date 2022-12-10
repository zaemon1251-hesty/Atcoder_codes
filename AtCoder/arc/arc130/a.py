N = int(input())
S = list(input())
t = []
cont = 1
ans = 0
for i in range(1, N):
    if S[i] == S[i-1]:
        cont += 1
    else:
        ans += cont * (cont - 1) // 2
        cont = 1
else:
    ans += cont * (cont - 1) // 2
print(ans)
