S = input()
nS = S.rstrip("a")
ar = len(S) - len(nS)
al = 0
while al < len(S) and S[al] == "a":
    al += 1
if al > ar:
    pass
else:
    S = nS + "a" * al
flg = True
N = len(S)
for i in range(N // 2):
    if S[i] != S[N - 1 - i]:
        flg = False
print("Yes" if flg else "No")
