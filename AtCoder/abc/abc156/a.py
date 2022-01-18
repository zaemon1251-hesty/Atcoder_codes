N, R = map(int, input().split())
if N >= 10:
    ans = R
else:
    ans = 100 * (10 - N) + R
print(ans)
