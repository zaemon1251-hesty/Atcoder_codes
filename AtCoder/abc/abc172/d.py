N = int(input())
ans = 0
for k in range(1, N+1):
    t = N//k
    ans += k*t*(t+1)//2
print(ans)
