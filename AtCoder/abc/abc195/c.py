N = int(input())
t = 3
ans = 0
while N >= pow(10, t):
    if N < pow(10, t + 3):
        ans += (t // 3) * (N - pow(10, t) + 1)
        break
    ans += (t // 3) * (pow(10, t + 3) - pow(10, t))
    t += 3
print(ans)
