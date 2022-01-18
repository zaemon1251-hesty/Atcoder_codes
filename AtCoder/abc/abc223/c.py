N = int(input())
S = []
took = 0
for _ in range(N):
    t = list(map(int, input().split()))
    S.append(t)
    took += t[0]/t[1]
half = took/2
i = 0
ans = 0
while half > 0:
    tmp = S[i][0]/S[i][1]
    if half > tmp:
        ans += S[i][0]
        half -= tmp
    else:
        ans += S[i][1]*half
        half = 0
    i += 1
print(ans)
