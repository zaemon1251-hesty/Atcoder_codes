S, T = input(), input()

N, M = len(S), len(T)
ans = M+1
for st in range(0, N-M+1):
    err = 0
    for j in range(st, st+M):
        if S[j] != T[j-st]:
            err += 1
    ans = min(ans, err)
print(ans)
