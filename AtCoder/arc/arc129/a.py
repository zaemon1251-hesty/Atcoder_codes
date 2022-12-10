N, L, R = map(int, input().split())
t = 1
ans = 0
while t <= N:
    if not((t << 1)-1 < L or R < t):
        if (N & t) != 0:
            ans += min(R, (t << 1) - 1) - max(L, t) + 1
    t <<= 1
print(ans)
