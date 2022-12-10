N = int(input())
S = list(map(int, input().split()))
ans = 0
highest = 0
for i in range(N):
    if S[i] < highest:
        ans += highest - S[i]
    else:
        highest = S[i]
print(ans)
