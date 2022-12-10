N = int(input())
C = []
for i in range(N):
    t, l, r = map(int, input().split())
    if t == 1:
        pass
    elif t == 2:
        r -= 0.1
    elif t == 3:
        l += 0.1
    else:
        l += 0.1
        r -= 0.1
    C.append([l,r])
ans = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        al, ar = C[i]
        bl, br = C[j]
        if al <= br <= ar or bl <= ar <= br:
            ans += 1
print(ans)
